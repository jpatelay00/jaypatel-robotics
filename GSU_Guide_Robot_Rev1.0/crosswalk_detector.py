from enum import Enum
from pathlib import Path
import numpy as np
from config import CROSSWALK_CONFIDENCE
class CrosswalkSignal(Enum): WALK='walk'; DONT_WALK='dont_walk'; UNKNOWN='unknown'
class CrosswalkDetector:
    LABELS=[CrosswalkSignal.DONT_WALK,CrosswalkSignal.UNKNOWN,CrosswalkSignal.WALK]
    def __init__(self,model_path='models/crosswalk.tflite'):
        self.minimum_confidence=CROSSWALK_CONFIDENCE; self.model_path=Path(model_path); self.interpreter=None; self.load_model()
    @property
    def ready(self):return self.interpreter is not None
    def load_model(self):
        if not self.model_path.exists(): print('Crosswalk model: WORK IN PROGRESS -',self.model_path); return
        try:
            try: from tflite_runtime.interpreter import Interpreter
            except ImportError: from tensorflow.lite.python.interpreter import Interpreter
            self.interpreter=Interpreter(model_path=str(self.model_path)); self.interpreter.allocate_tensors(); self.input_info=self.interpreter.get_input_details()[0]; self.output_info=self.interpreter.get_output_details()[0]
        except Exception as e: print('Crosswalk model unavailable:',e); self.interpreter=None
    def detect(self,frame):
        if frame is None or not self.ready:return CrosswalkSignal.UNKNOWN,0.0
        try:
            info=self.input_info; h,w=int(info['shape'][1]),int(info['shape'][2]); ys=np.linspace(0,frame.shape[0]-1,h).astype(int); xs=np.linspace(0,frame.shape[1]-1,w).astype(int); image=frame[ys][:,xs]; image=np.expand_dims(image,0).astype(info['dtype'])
            if info['dtype']==np.float32:image=image/255.0
            self.interpreter.set_tensor(info['index'],image); self.interpreter.invoke(); scores=np.squeeze(self.interpreter.get_tensor(self.output_info['index'])).astype(float)
            if scores.size!=3:return CrosswalkSignal.UNKNOWN,0.0
            i=int(np.argmax(scores)); conf=float(scores[i]); signal=self.LABELS[i]
            return (signal,conf) if conf>=self.minimum_confidence else (CrosswalkSignal.UNKNOWN,conf)
        except Exception as e: print('Crosswalk inference error:',e); return CrosswalkSignal.UNKNOWN,0.0
    def safe_to_cross(self,frame):
        signal,conf=self.detect(frame); return signal==CrosswalkSignal.WALK and conf>=self.minimum_confidence

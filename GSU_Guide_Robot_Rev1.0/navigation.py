import time
from motor_control import MotorController
from sensors import Sensors
from movement import Movement
from camera import RobotCamera
from crosswalk_detector import CrosswalkDetector
from street_crossing import StreetCrossing
from routes import ROUTES
from logger import RunLogger
class Navigator:
    def __init__(self):
        self.motors=MotorController(); self.sensors=Sensors(self.motors); self.movement=Movement(self.motors,self.sensors); self.camera=RobotCamera(); self.crosswalk_detector=CrosswalkDetector(); self.street_crossing=StreetCrossing(self.camera,self.crosswalk_detector,self.motors); self.logger=RunLogger(); self.running=False; self.destination=None
    def navigate(self,destination,allow_test=False):
        destination=destination.lower().strip(); route=ROUTES.get(destination)
        if not route: print('Unknown destination:',destination); return False
        if route['status']!='READY' and not (allow_test and route['status']=='TEST'):
            print('\n*** WORK IN PROGRESS ***'); print('Destination:',destination); print('Start point:',route['start']); return False
        self.destination=destination; self.running=True; self.logger.record(destination,'start',self.motors,self.sensors,force=True)
        try:
            for command,value in route['steps']:
                if not self.running:return False
                print(command,value)
                if command=='forward':self._forward_logged(value)
                elif command=='backward':self.movement.backward(value)
                elif command=='left':self.movement.left(value)
                elif command=='right':self.movement.right(value)
                elif command=='wait':time.sleep(float(value))
                elif command=='checkpoint':
                    path=self.camera.save_photo(str(value)); self.logger.record(destination,'checkpoint',self.motors,self.sensors,str(path),True)
                elif command=='crossing':
                    self.motors.stop()
                    if not self.street_crossing.request_crossing(): print('Crossing not approved'); self.stop(); return False
                    self._forward_logged(value)
                else: print('Unknown route command:',command); self.stop(); return False
            self.logger.record(destination,'arrived',self.motors,self.sensors,force=True); self.stop(); print('Arrived at',destination); return True
        except KeyboardInterrupt:self.stop(); return False
    def _forward_logged(self,cm):
        from config import DRIVE_STEP_CM
        remaining=abs(float(cm))
        while remaining>0:
            self.movement.wait_for_clear_path(); step=min(DRIVE_STEP_CM,remaining); self.motors.forward(step); remaining-=step; self.logger.record(self.destination,'forward',self.motors,self.sensors)
    def stop(self):self.running=False; self.movement.stop()
    def status(self):
        return {'running':self.running,'destination':self.destination,'distance_cm':round(self.sensors.distance_cm(),1),'fake_motors':self.motors.fake,'camera':self.camera.camera is not None,'crosswalk_model':self.crosswalk_detector.ready,'log_file':str(self.logger.path)}
    def close(self):self.stop(); self.camera.close()

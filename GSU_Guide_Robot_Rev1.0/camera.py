from pathlib import Path
from datetime import datetime
from config import CAMERA_WIDTH, CAMERA_HEIGHT

class RobotCamera:
    def __init__(self):
        self.camera = None
        try:
            from picamera2 import Picamera2
            self.camera = Picamera2()
            cfg = self.camera.create_preview_configuration(
                main={"size": (CAMERA_WIDTH, CAMERA_HEIGHT)}
            )
            self.camera.configure(cfg)
            self.camera.start()
        except Exception as e:
            print("Camera unavailable:", e)

    def capture_array(self):
        if self.camera is None: return None
        try: return self.camera.capture_array()
        except Exception as e:
            print("Camera capture failed:", e)
            return None

    def save_photo(self, label="photo"):
        if self.camera is None: return None
        Path("photos").mkdir(exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = Path("photos") / f"{label}_{stamp}.jpg"
        self.camera.capture_file(str(path))
        return str(path)

    def close(self):
        if self.camera:
            try: self.camera.stop()
            except Exception: pass

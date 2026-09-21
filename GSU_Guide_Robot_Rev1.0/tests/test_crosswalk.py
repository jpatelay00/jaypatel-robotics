from camera import RobotCamera
from crosswalk_detector import CrosswalkDetector
c=RobotCamera();d=CrosswalkDetector();print('Camera:',c.camera is not None,'Model:',d.ready);s,conf=d.detect(c.capture_array());print(s.value,conf);c.close()

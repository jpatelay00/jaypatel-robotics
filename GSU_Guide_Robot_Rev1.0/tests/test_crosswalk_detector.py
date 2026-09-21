from camera import RobotCamera
from crosswalk_detector import CrosswalkDetector
c = RobotCamera()
d = CrosswalkDetector()
frame = c.capture_array()
signal, confidence = d.detect(frame)
print("Signal:", signal.value)
print("Confidence:", confidence)
print("Safe:", d.safe_to_cross(frame))
c.close()

import time
from motor_control import MotorController
from sensors import Sensors
m = MotorController()
s = Sensors(m)
try:
    while True:
        print("Distance:", s.distance_cm(), "cm")
        time.sleep(0.5)
except KeyboardInterrupt:
    m.stop()

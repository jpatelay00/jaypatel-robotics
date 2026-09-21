import time
from config import STOP_DISTANCE_CM, DRIVE_STEP_CM

class Movement:
    def __init__(self, motors, sensors):
        self.motors = motors
        self.sensors = sensors

    def wait_for_clear_path(self):
        while not self.sensors.path_clear(STOP_DISTANCE_CM):
            self.motors.stop()
            print("Obstacle:", self.sensors.distance_cm(), "cm")
            time.sleep(0.2)

    def forward(self, cm):
        remaining = abs(float(cm))
        while remaining > 0:
            self.wait_for_clear_path()
            step = min(DRIVE_STEP_CM, remaining)
            self.motors.forward(step)
            remaining -= step

    def backward(self, cm): self.motors.backward(cm)
    def left(self, deg): self.motors.left(deg)
    def right(self, deg): self.motors.right(deg)
    def stop(self): self.motors.stop()

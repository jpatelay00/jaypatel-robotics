import time
from config import MOTOR_SPEED, TURN_SPEED, ALLOW_FAKE_HARDWARE

class FakeGoPiGo:
    def set_speed(self, speed): print("[fake] speed", speed)
    def drive_cm(self, cm):
        print("[fake] drive", cm, "cm")
        time.sleep(0.1)
    def turn_degrees(self, deg):
        print("[fake] turn", deg, "degrees")
        time.sleep(0.1)
    def stop(self): print("[fake] stop")

class MotorController:
    def __init__(self):
        self.fake = False
        try:
            import easygopigo3 as easy
            self.gpg = easy.EasyGoPiGo3()
            self.gpg.set_speed(MOTOR_SPEED)
        except Exception as e:
            if not ALLOW_FAKE_HARDWARE:
                raise
            print("GoPiGo3 unavailable:", e)
            self.fake = True
            self.gpg = FakeGoPiGo()

    def forward(self, cm):
        self.gpg.set_speed(MOTOR_SPEED)
        self.gpg.drive_cm(abs(float(cm)))

    def backward(self, cm):
        self.gpg.set_speed(MOTOR_SPEED)
        self.gpg.drive_cm(-abs(float(cm)))

    def left(self, degrees):
        self.gpg.set_speed(TURN_SPEED)
        self.gpg.turn_degrees(-abs(float(degrees)))
        self.gpg.set_speed(MOTOR_SPEED)

    def right(self, degrees):
        self.gpg.set_speed(TURN_SPEED)
        self.gpg.turn_degrees(abs(float(degrees)))
        self.gpg.set_speed(MOTOR_SPEED)

    def stop(self):
        self.gpg.stop()

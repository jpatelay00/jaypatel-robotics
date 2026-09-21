class FakeDistanceSensor:
    def read(self): return 999

class Sensors:
    def __init__(self, motors):
        if motors.fake:
            self.distance_sensor = FakeDistanceSensor()
        else:
            try:
                self.distance_sensor = motors.gpg.init_distance_sensor("I2C")
            except Exception as e:
                print("Distance sensor unavailable:", e)
                self.distance_sensor = FakeDistanceSensor()

    def distance_cm(self):
        try:
            return float(self.distance_sensor.read())
        except Exception:
            return 999.0

    def path_clear(self, minimum):
        d = self.distance_cm()
        return d <= 0 or d > minimum

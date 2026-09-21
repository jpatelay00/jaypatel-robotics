import time
from crosswalk_detector import CrosswalkSignal
from config import REQUIRE_MANUAL_CROSSING_APPROVAL

class StreetCrossing:
    def __init__(self, camera, detector, motors):
        self.camera = camera
        self.detector = detector
        self.motors = motors

    def observe_signal(self):
        frame = self.camera.capture_array()
        return self.detector.detect(frame)

    def wait_for_walk_signal(self):
        self.motors.stop()
        while True:
            signal, confidence = self.observe_signal()
            print("Signal:", signal.value, "confidence:", round(confidence, 2))
            if signal == CrosswalkSignal.WALK and confidence >= self.detector.minimum_confidence:
                return True
            time.sleep(0.25)

    def request_crossing(self):
        self.motors.stop()

        if REQUIRE_MANUAL_CROSSING_APPROVAL:
            signal, confidence = self.observe_signal()
            print("Camera:", signal.value, round(confidence, 2))
            print("*** STREET CROSSING TEST - MANUAL APPROVAL REQUIRED ***")
            return input("Type CROSS to approve: ").strip() == "CROSS"

        return self.wait_for_walk_signal()

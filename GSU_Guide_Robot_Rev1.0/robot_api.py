"""Stable interface for the separate phone/web application."""
from navigation import Navigator
from routes import ROUTES
class RobotAPI:
    def __init__(self):self.navigator=Navigator()
    def destinations(self):return [n for n in ROUTES if not n.startswith('_')]
    def go_to(self,destination):return self.navigator.navigate(destination)
    def stop(self):self.navigator.stop(); return True
    def status(self):return self.navigator.status()
    def close(self):self.navigator.close()

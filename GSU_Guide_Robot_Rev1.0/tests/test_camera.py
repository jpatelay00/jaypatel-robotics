from camera import RobotCamera
c = RobotCamera()
print("Saved:", c.save_photo("test"))
c.close()

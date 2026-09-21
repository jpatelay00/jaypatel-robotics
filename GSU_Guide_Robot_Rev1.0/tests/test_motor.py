from motor_control import MotorController
m = MotorController()
print("Fake:", m.fake)
m.forward(20)
m.right(45)
m.left(45)
m.backward(10)
m.stop()

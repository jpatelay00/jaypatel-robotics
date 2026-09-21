from motor_control import MotorController
m=MotorController(); print('Fake:',m.fake)
if input('Clear floor. Type MOVE: ')=='MOVE':m.forward(10);m.right(90);m.left(90);m.backward(10)
m.stop()

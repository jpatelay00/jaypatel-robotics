from navigation import Navigator
r=Navigator(); print(r.status()); print('Distance:',r.sensors.distance_cm(),'cm'); print('Photo:',r.camera.save_photo('hardware_test')); r.close()

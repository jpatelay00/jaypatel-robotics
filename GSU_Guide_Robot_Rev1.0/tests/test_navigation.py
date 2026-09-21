from navigation import Navigator
from routes import ROUTES
ROUTES['_controlled_test']={'status':'TEST','start':'controlled area','steps':[('forward',20),('right',45),('forward',20),('left',45)]}
n=Navigator()
if input('Type TEST to move robot: ')=='TEST':n.navigate('_controlled_test',allow_test=True)
n.close()

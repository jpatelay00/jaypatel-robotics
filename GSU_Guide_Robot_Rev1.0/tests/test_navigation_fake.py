from navigation import Navigator
from routes import ROUTES

ROUTES["test"] = {
    "status": "READY",
    "start": "test",
    "steps": [("forward",20),("right",45),("forward",20),("left",45),("backward",10)]
}
n = Navigator()
n.navigate("test")
n.close()

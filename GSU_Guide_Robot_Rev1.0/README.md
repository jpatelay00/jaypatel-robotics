# GSU Guide Robot - Base v2

This is the stripped-down base project for the GoPiGo3 guide robot.

There is no microphone or speech-recognition code. A separate app can eventually
send destinations through `RobotAPI.go_to(destination)`.

## Structure

- `motor_control.py` - direct GoPiGo3 motor control
- `sensors.py` - Dexter distance sensor
- `movement.py` - movement plus obstacle stopping
- `camera.py` - Raspberry Pi Camera Module 2
- `crosswalk_detector.py` - WALK / DONT_WALK / UNKNOWN recognition interface
- `street_crossing.py` - crossing state/safety layer
- `navigation.py` - route execution
- `routes.py` - measured routes
- `robot_api.py` - clean interface for the separate app
- `tests/` - hardware/module tests

## WORK IN PROGRESS

The exact GSU routes and the actual pedestrian-signal recognition model are
intentionally unfinished.

The crosswalk detector currently returns `UNKNOWN`. It will never fake a WALK
result. The correct next step is to collect photos/video of the actual
pedestrian signals on the routes, train/test a small model, and put only its
inference code into `crosswalk_detector.py`.

`REQUIRE_MANUAL_CROSSING_APPROVAL` is also True by default. Leave it that way
during development.

A green walking symbol by itself does not prove that a street is physically
clear. Autonomous street crossing would also require substantially more
perception/testing, including vehicle, curb/drop-off and localization handling.

## App integration

The future app can use:

```python
from robot_api import RobotAPI

robot = RobotAPI()
print(robot.destinations())
robot.go_to("library north")
robot.stop()
```

A REST/WebSocket/MQTT server can later wrap this interface without changing the
motor or navigation modules.

## Tests

From the project folder:

```bash
python3 tests/test_camera.py
python3 tests/test_distance_sensor.py
python3 tests/test_motor.py
python3 tests/test_crosswalk_detector.py
python3 tests/test_navigation_fake.py
```

Exact route distances/angles should only be changed to `READY` after physical
measurement and testing.

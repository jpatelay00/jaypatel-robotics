# Exact campus measurements are WORK IN PROGRESS.
# Commands: forward/backward (cm), left/right (degrees), wait (seconds),
# checkpoint (name), crossing (distance in cm).

ROUTES = {
    "library north": {"status": "WORK IN PROGRESS", "start": "WORK IN PROGRESS", "steps": []},
    "classroom south": {"status": "WORK IN PROGRESS", "start": "WORK IN PROGRESS", "steps": []},
    "aderhold": {"status": "WORK IN PROGRESS", "start": "WORK IN PROGRESS", "steps": []},
    "student center": {"status": "WORK IN PROGRESS", "start": "WORK IN PROGRESS", "steps": []},

    "_example": {
        "status": "EXAMPLE",
        "start": "placeholder",
        "steps": [
            ("forward", 200),
            ("right", 90),
            ("forward", 300),
            ("checkpoint", "intersection_1"),
            ("crossing", 500),
            ("left", 90),
            ("forward", 200)
        ]
    }
}

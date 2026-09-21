from navigation import Navigator
from routes import ROUTES

nav = Navigator()

try:
    print("GSU Guide Robot")
    for name in ROUTES:
        if not name.startswith("_"):
            print("-", name)

    while True:
        destination = input("\nDestination (or quit): ").strip().lower()
        if destination == "quit":
            break
        nav.navigate(destination)
finally:
    nav.close()

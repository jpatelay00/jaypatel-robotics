import csv, time
from pathlib import Path
from datetime import datetime
class RunLogger:
    def __init__(self, interval=0.4):
        Path('data').mkdir(exist_ok=True); self.interval=interval; self.last=0.0
        self.path=Path('data')/('run_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'.csv')
        with self.path.open('w',newline='') as f: csv.writer(f).writerow(['timestamp','destination','command','left_encoder','right_encoder','distance_cm','note'])
    def record(self,destination,command,motors,sensors,note='',force=False):
        now=time.monotonic()
        if not force and now-self.last<self.interval:return
        self.last=now
        try:left,right=motors.gpg.read_encoders()
        except Exception:left=right=0
        with self.path.open('a',newline='') as f: csv.writer(f).writerow([datetime.now().isoformat(timespec='milliseconds'),destination,command,left,right,sensors.distance_cm(),note])

import json
import datetime
from time import sleep
from aw_core.models import Event
from aw_client import ActivityWatchClient

# configure the following variables to your needs
bucket_id = "wakatime"
filepath = "/path/to/wakatime-heartbeats.json"
pulsetime = 300 # merges heartbeats that are within 5 minutes of each other

client = ActivityWatchClient("aw-wakatime")
client.connect()

client.create_bucket(bucket_id, event_type="app.editor.activity")

file = open(filepath, "r")
obj = json.load(file)

# decrease this only if not all events are being sent
sleep_after_events = 100
count = 0

for day in range(len(obj["days"])):
    for heartbeat in obj["days"][day]["heartbeats"]:
        heartbeat_data = dict()
        datetime_created_at = datetime.datetime.strptime(heartbeat["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        heartbeat_data.update({"project": heartbeat["project"], "file": heartbeat["entity"], "language": heartbeat["language"]})
        event = Event(timestamp=heartbeat["created_at"], data=heartbeat_data)
        client.heartbeat(bucket_id, event=event, pulsetime=pulsetime, queued=True)
        count +=1
        if count % sleep_after_events == 0:
            sleep(1)

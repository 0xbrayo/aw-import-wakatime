from calendar import c
import json

from aw_core.models import Event
from aw_client import ActivityWatchClient
from more_itertools import bucket

client = ActivityWatchClient("aw-wakatime")
client.connect()

bucket_id = "wakatime"
client.create_bucket(bucket_id) # customize this to your needs

filepath = "/path/to/your/wakatime-heartbeats.json"

file = open(filepath, "r")
obj = json.load(file)

for heartbeat in obj["days"][0]["heartbeats"]:
    event_data = dict()
    event_data.update({"project": heartbeat["project"], "filename": heartbeat["entity"], "language": heartbeat["language"], "time": heartbeat["time"]})
    event = Event(timestamp=heartbeat["created_at"],duration=heartbeat["time"], data=event_data)
    client.insert_event(bucket_id, event=event)
    client.heartbeat(bucket_id, event=event, pulsetime=1,commit_interval=10)

import json

def toJson(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4))


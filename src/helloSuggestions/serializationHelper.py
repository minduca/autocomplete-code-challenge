import json

# A simple generic serializer. All it does is to converts a complex object into a python object that is serializable.
def toJson(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4))


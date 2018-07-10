import json

# I found a well stablished serializer for python called Marshmallow.  However,
# since the problem don't have a lot of requirements I chose not to add
# unecessary dependencies just for this.  All it does is
# to converts a complex object into a python object that is serializable.
def toJson(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4))


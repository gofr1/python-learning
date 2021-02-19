import msgpack # schemaless binary format
from datetime import datetime

type_key = '__type__'
datetime_type = 'datetime'

def default(obj): # serializing
    if isinstance(obj, datetime):
        return {
            type_key: datetime_type,
            'value': obj.isoformat(),
        }
    return obj

def object_hook(obj): # deserializing
    if obj.get(type_key) == datetime_type:
        return datetime.fromisoformat(obj['value'])
    return obj

metric = {
    'time': datetime.now(),
    'name': 'memory',
    'value': 3.14,
    'labels': {
        'host': 'prod7',
        'version': '1.3.4',
    },
}

# use msgpack to serialize
data = msgpack.dumps(metric, default=default)
print('data size:', len(data))
#* data size: 118

# and deserialized
metric2 = msgpack.loads(data, object_hook=object_hook)
print('metric2 equal:', metric2 == metric)
#* metric2 equal: True

# Let's compare with json
import json

jdata = json.dumps(metric, default=default)
ratio = len(data)/len(jdata)
print(f'ratio msgp/json: {ratio:=4.2%}')
import os
os.chdir('./serialization/json')

from event import event
import json

data = json.dumps(event, indent=4)
print(data)
#* {
#*     "name": "John Doe",
#*     "purchase date": "2021-02-15T10:08:15.561Z",
#*     "items": [
#*         {
#*             "item": "Beer",
#*             "amount": 6,
#*             "price": 2.99
#*         },
#*         {
#*             "item": "Bread",
#*             "amount": 2,
#*             "price": 1.95
#*         },
#*         {
#*             "item": "Water",
#*             "amount": 5,
#*             "price": 0.54
#*         }
#*     ]
#* }

type(data)
#* <class 'str'>

data_bytes = data.encode('utf-8')
type(data_bytes)
#* <class 'bytes'>

event_str = json.loads(data)
print(event_str == event)
#* True

# write into file
with open('event.json', 'w') as out:
    json.dump(event, out)

# read json from file
with open('event.json', 'r') as fp:
    event_file = json.load(fp)

print(event_file == event)
#* True
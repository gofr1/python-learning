import os
os.chdir('./serialization/json')

from purchases import event
import json

data = json.dumps(event, indent=4)
#* TypeError: Object of type datetime is not JSON serializable

from custom import default

data = json.dumps(event, default = default, indent=4)
# Now it works

json.loads(data)
#* {'purchases': [
#* {'name': 'John Doe', 'purchase date': '2021-02-15T10:08:15.000561',  'items': [{...}]}, 
#* {'name': 'Jack Holmes', 'purchase date': '2021-02-10T08:19:34.000786', 'items': [{...}]}
#* ]}

from custom import pairs_hook

json.loads(data, object_pairs_hook = pairs_hook)
#* {'purchases': [
#* {'name': 'John Doe', 'purchase date': datetime.datetime(2021, 2, 15, 10, 8, 15, 561), 'items': [{...}]}, 
#* {'name': 'Jack Holmes', 'purchase date': datetime.datetime(2021, 2, 10, 8, 19, 34, 786), 'items': [{...}]}]}
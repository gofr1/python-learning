import json
from io import BytesIO

groups = [
    {'animal': 'bee', 'group': 'swarm'},
    {'animal': 'fox', 'group': 'skulk'},
    {'animal': 'whale', 'group': 'pod'},
    {'animal': 'wolf', 'group': 'pack'}
]

# Emulate a network

# sending
network = BytesIO()
for message in groups:
    data = json.dumps(message)
    network.write(data.encode('utf-8'))
    network.write(b'\n')

# receiving
network.seek(0) # go back to start of data to read
# to the beginning of the buffer

while True: # use this because we don't know how many lines to come in
    line = network.readline()
    if not line:
        break

    message = json.loads(line)
    print(f'got {message}')
#* got {'animal': 'bee', 'group': 'swarm'}
#* got {'animal': 'fox', 'group': 'skulk'}
#* got {'animal': 'whale', 'group': 'pod'}
#* got {'animal': 'wolf', 'group': 'pack'}
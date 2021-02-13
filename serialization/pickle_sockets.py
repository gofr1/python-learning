import pickle, os
from socket import socketpair

os.chdir('./serialization')
os.getcwd()

from pickle_basics import move0, move1, move2, move3

# Defime sockets for writing and reading
ws,rs = socketpair()
w, r = ws.makefile('wb'), rs.makefile('rb')

# Serialize
pickle.dump(move0, w)
pickle.dump(move1, w)
pickle.dump(move2, w)
pickle.dump(move3, w)
w.flush() # send to another socket

# De-serialize
for _ in range(4):
    move = pickle.load(r)
    print(f'{move.limb} {move.what}')
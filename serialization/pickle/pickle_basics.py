from datetime import datetime, timedelta
import pickle

class Move:
    def __init__(self, time, limb, what) -> None:
        self.time = time
        self.limb = limb
        self.what = what
    
    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f'{cls}({self.time!r}, {self.limb!r}, {self.what!r})'

second = timedelta(seconds = 1)
now = datetime.now()

move0 = Move(now + 1*second, 'jump', 'to the left')
move1 = Move(now + 2*second, 'step', 'to the right')
move2 = Move(now + 3*second, 'hands', 'on your hips')
move3 = Move(now + 4*second, 'knees', 'bring in tight')

# dumps and loads used for objects
data = pickle.dumps(move0)
data
#* b'\x80\x04\x95p\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x04Move\x94\x93\x94)\x81\x94}
#* \x94(\x8c\x04time\x94\x8c\x08datetime\x94\x8c\x08datetime\x94\x93\x94C\n\x07\xe5\x02\r\x0f*6\rb|\
#* x94\x85\x94R\x94\x8c\x04limb\x94\x8c\x04jump\x94\x8c\x04what\x94\x8c\x0bto the left\x94ub.'

type(data)
#* <class 'bytes'>

move1d = pickle.loads(data)
move1d
#* Move(datetime.datetime(2021, 2, 13, 15, 34, 51, 935433), 'jump', 'to the left')

# dump and load used for files
with open('move1.pkl', 'wb') as out:
    pickle.dump(move1, out)

with open('move1.pkl', 'rb') as fp:
    move1f = pickle.load(fp)

move1f
#* Move(datetime.datetime(2021, 2, 13, 15, 42, 55, 877180), 'step', 'to the right')


dance = [move0, move1, move2, move3]
with open('dance.pkl', 'wb') as out:
    pickle.dump(dance, out)
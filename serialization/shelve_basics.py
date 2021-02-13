import shelve, os

#os.chdir('./serialization')
#os.getcwd()

from pickle_basics import move0, move1, move2, move3

db = shelve.open('dance.db') # Key-value store
db['0'] = move0
db['1'] = move1
db['2'] = move2
db['3'] = move3
db.close()

# ...

db = shelve.open('dance.db')
print(db['0'])
#* Move(datetime.datetime(2021, 2, 13, 16, 1, 43, 752192), 'jump', 'to the left')
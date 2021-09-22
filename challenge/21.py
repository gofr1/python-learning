#21

# Let's work with zip from the previous task
from zipfile import ZipFile, ZipInfo

with ZipFile('bin.zip', 'r') as zout:
    zout.namelist()
#* ['readme.txt', 'package.pack']

with ZipFile('bin.zip', 'r') as zout:
    print(zout.read('readme.txt', pwd=bytes('invader'[::-1].encode())).decode('utf-8'))

#* Yes! This is really level 21 in here. 
#* And yes, After you solve it, you'll be in level 22!
#* 
#* Now for the level:
#* 
#* * We used to play this game when we were kids
#* * When I had no idea what to do, I looked backwards.

with ZipFile('bin.zip', 'r') as zout:
    print(zout.read('package.pack', pwd=bytes('invader'[::-1].encode())).decode('ISO-8859-1'))
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x9c in position 1: invalid start byte
# Let's change to some different
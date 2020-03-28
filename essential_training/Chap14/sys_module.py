#!/usr/bin/env python3

# import whole modules
import sys, os 
# import some methods from modules
from datetime import datetime 
from random import shuffle

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))

    p = sys.platform
    print(f'Platform: {p}')

    o = os.name
    print(f'OS name: {o}')
    
    pa = os.getenv('PATH')
    print(f'PATH var: {pa}')

    wd = os.getcwd()
    print(f'Current working directory is: {wd}')

    rnd = os.urandom(25).hex() # 25 byte object
    print(rnd)
    
    x = list(range(25))
    print(x)
    shuffle(x)
    print(x)

    now = datetime.now()
    print(f'Current date and time is: {now}')
    print(now.year, now.month, now.day, now.hour, now.minute, now.second)

if __name__ == '__main__':
    main()
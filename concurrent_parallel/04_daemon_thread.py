#!/usr/bin/env python3

import time
import threading

def cleaner(): 
    while True:
        print('Cleaning...')
        time.sleep(1)

if __name__ == '__main__':
    clean = threading.Thread(target=cleaner) # daemon thread
    clean.daemon = True
    clean.start() 

    print('Doing something...')
    time.sleep(0.6)
    print('Doing something...')
    time.sleep(0.6)
    print('Doing something...')
    time.sleep(0.6)
    print('Done')

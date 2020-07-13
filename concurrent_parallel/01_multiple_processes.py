#!/usr/bin/env python3

import os
import threading
import multiprocessing as mp

# simple function that wastes CPU cycles forever
def cpu_waster():
    while True:
        pass

print(f'__name__ is {__name__}')

if __name__ == '__main__':
    # display info about process
    print(f'\n Process ID: {os.getpid()}')
    print(f'Thread count: {threading.active_count()}')
    for thread in threading.enumerate():
        print(thread)
    
    print('\nStarting 2 CPU wasters...')
    for _ in range(2):
        mp.Process(target=cpu_waster).start()
    
    # display info about process
    print(f'\n Process ID: {os.getpid()}')
    print(f'Thread count: {threading.active_count()}')
    for thread in threading.enumerate():
        print(thread)
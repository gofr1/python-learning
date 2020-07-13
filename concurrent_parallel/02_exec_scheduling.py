#!/usr/bin/env python3

import time
import threading

chopping = True

def vegetable_cutter():
    name = threading.current_thread().getName()
    vegetable_count = 0
    while chopping:
        print(f'{name} chop a vegetable!')
        vegetable_count += 1
    print(f'{name} chopped {vegetable_count} vegetables.' )

if __name__ == '__main__':
    threading.Thread(target=vegetable_cutter, name='Gordon Freeman').start()
    threading.Thread(target=vegetable_cutter, name='Alyx Vance').start()

    time.sleep(1) # wait for one second
    chopping = False # stop both threads 

#!/usr/bin/env python3

import time
import threading

class ChefAlyx(threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        print('Alyx started and waiting...')
        time.sleep(3)
        print('Alyx is done')
    
# main thread
if __name__ == '__main__':
    print('Gordon started and requested Alyx\'s help')
    alyx = ChefAlyx()
    print(f'\tAlyx alive?: {alyx.is_alive()}')

    print('Gordon tells Alyx to start')
    alyx.start()
    print(f'\tAlyx alive?: {alyx.is_alive()}')

    print('Gordon continues')
    time.sleep(0.5)
    print(f'\tAlyx alive?: {alyx.is_alive()}')

    print('Gordon waits for Alyx to join ...')
    alyx.join()
    print(f'\tAlyx alive?: {alyx.is_alive()}')

    print('Gordon and Alyx are both done!')
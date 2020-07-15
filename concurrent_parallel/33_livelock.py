#!/usr/bin/env python3

import threading
# to over come livelock
# we will us some random and time ...
import time
from random import random

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()

sushi_count = 500

def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    while sushi_count > 0:
        first_chopstick.acquire()
        if not second_chopstick.acquire(blocking=False):
            print(f'{name} released their first chopstick')
            first_chopstick.release()
            time.sleep(random()/10) # ... here
        else:
            try:
                if sushi_count > 0:
                    sushi_count -= 1
                    print(f'{name} took a piece! Sushi remaining {sushi_count}')
            finally:
                second_chopstick.release()
                first_chopstick.release()

if __name__ == '__main__':
    threading.Thread(target=philosopher, args=('Gordon', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=('Alyx', chopstick_b, chopstick_c)).start()
    threading.Thread(target=philosopher, args=('Barny', chopstick_c, chopstick_a)).start() 


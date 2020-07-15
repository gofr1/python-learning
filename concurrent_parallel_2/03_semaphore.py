#!/usr/bin/env python3

import threading
import random
import time

charger =threading.Semaphore(4)

def cellphone():
    name = threading.current_thread().getName()
    #charger.acquire()
    with charger:
        print(f'{name} is charging...')
        time.sleep(random.uniform(1,2))
        print(f'{name} is done charging!')
    #charger.release()

if __name__ == '__main__':
    for phone in range(10):
        threading.Thread(target=cellphone, name=f'Phone-{phone}').start()

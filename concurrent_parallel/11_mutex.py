#!/usr/bin/env python3

import threading
import time

garlic_count = 0
pencil = threading.Lock() # 0 use a lock

# def shopper():
#     global garlic_count
#     pencil.acquire() # 1 acquire a lock
#     for _ in range(5): # with rows where you see number in comments in can handle all 10 millions w/o data race
#         print(f'{threading.current_thread().getName()} is thinking')
#         time.sleep(0.5)
#         garlic_count += 1
#     pencil.release() # 2 release a lock

# that way problenm will run faster 
def shopper():
    global garlic_count
    for _ in range(5): 
        print(f'{threading.current_thread().getName()} is thinking')
        time.sleep(0.5)
        pencil.acquire() 
        garlic_count += 1
        pencil.release() 

if __name__ == '__main__':
    gordon = threading.Thread(target=shopper)
    alyx = threading.Thread(target=shopper)

    gordon.start()
    alyx.start()

    gordon.join()
    alyx.join()

    print(f'We should by {garlic_count}')

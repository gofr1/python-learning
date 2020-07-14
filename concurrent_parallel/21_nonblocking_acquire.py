#!/usr/bin/env python3

import threading
import time

items_on_notepad = 0
pencil = threading.Lock()

def shopper():
    global items_on_notepad
    name = threading.current_thread().getName()
    items_to_add = 0
    while items_on_notepad <= 20:
        if items_to_add and pencil.acquire(blocking=False): # add items to shared items_on_notepad
            items_on_notepad += items_to_add
            print(f'{name} added {items_to_add} item(s) to notepad')
            items_to_add = 0
            time.sleep(0.3) # time spent writing
            pencil.release()
        else: # look for other things to buy
            time.sleep(0.1) # time spent searching
            items_to_add += 1
            print(f'{name} found something else to buy')

if __name__ == "__main__":
    gordon = threading.Thread(target=shopper, name='Gordon')
    alyx = threading.Thread(target=shopper, name='Alyx')

    start_time = time.perf_counter()

    gordon.start()
    alyx.start()

    gordon.join()
    alyx.join()
    
    elapsed_time = time.perf_counter() - start_time

    print(f'Elapsed time {elapsed_time:.2f} seconds')

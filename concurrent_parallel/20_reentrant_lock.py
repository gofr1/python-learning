#!/usr/bin/env python3

import threading

garlic_count = 0
potato_count = 0
pencil = threading.RLock() # Reentrant lock

# Lock can be released by a different thread than was used to acquire it
# RLock must be released by the samr thread that acquire it (as many times as it was acquired)

def add_garlic():
    global garlic_count
    pencil.acquire()
    garlic_count += 1
    pencil.release()

def add_potato():
    global potato_count
    pencil.acquire()
    potato_count += 1
    add_garlic()
    pencil.release()

def shopper():
    for _ in range(10_000):
        add_garlic()
        add_potato()

if __name__ == '__main__':
    gordon = threading.Thread(target=shopper)
    alyx = threading.Thread(target=shopper)

    gordon.start()
    alyx.start()

    gordon.join()
    alyx.join()

    print(f'We should by {garlic_count} garlic')
    print(f'We should by {potato_count} potatoes')

#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor
import time

def how_many_vegetables():
    print('Alyx is counting vegetables...')
    time.sleep(3)
    return 42

if __name__ == '__main__':
    print('Gordon asks Alyx how many vegetables are in the pantry.')
    with ThreadPoolExecutor() as pool:
        future = pool.submit(how_many_vegetables)
        print('Gordon can do other things while he waits for the result.')
        print(f'Alex responds with {future.result()}')
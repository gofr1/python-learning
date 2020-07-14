#!/usr/bin/env python3

import threading

garlic_count = 0

def shopper():
    global garlic_count
    for _ in range(10000000): # with 10 all works fine
        garlic_count += 1

if __name__ == '__main__':
    gordon = threading.Thread(target=shopper)
    alyx = threading.Thread(target=shopper)

    gordon.start()
    alyx.start()

    gordon.join()
    alyx.join()

    print(f'We should by {garlic_count}')

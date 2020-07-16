#!/usr/bin/env python3

import threading

bags_of_chips = 1 # start with one on the list
pencil = threading.Lock()

def cpu_work(work_units):
    x = 0
    for _ in range(work_units * 1_000_000):
        x += 1

def gordon_shopper():
    global bags_of_chips
    cpu_work(1) # do a bit work
    with pencil:
        bags_of_chips *= 2
        print('Gordon DOUBLED the bags of chips!')

def alyx_shopper():
    global bags_of_chips
    cpu_work(1) # do a bit work
    with pencil:
        bags_of_chips += 3
        print('Alyx ADDED 3 bags of chips!')

if __name__ == '__main__':
    shoppers = []
    for s in range(5):
        shoppers.append(threading.Thread(target=gordon_shopper))
        shoppers.append(threading.Thread(target=alyx_shopper))
    for s in shoppers:
        s.start()
    for s in shoppers:
        s.join()
    print(f'We need to buy {bags_of_chips} bags of chips!')

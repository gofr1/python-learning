#!/usr/bin/env python3

import threading

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()

sushi_count = 500

def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    while sushi_count > 0:
        first_chopstick.acquire()
        second_chopstick.acquire()

        if sushi_count > 0:
            sushi_count -= 1
            print(f'{name} took a piece! Sushi remaining {sushi_count}')
        
        second_chopstick.release()
        first_chopstick.release()

if __name__ == '__main__':
    threading.Thread(target=philosopher, args=('Gordon', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=('Alyx', chopstick_b, chopstick_c)).start()
    # deadlock exists here 
    #threading.Thread(target=philosopher, args=('Barny', chopstick_c, chopstick_a)).start() 
    # lets change
    threading.Thread(target=philosopher, args=('Barny', chopstick_a, chopstick_c)).start() 


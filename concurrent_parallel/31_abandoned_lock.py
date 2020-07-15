#!/usr/bin/env python3

import threading

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()

sushi_count = 500

def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    while sushi_count > 0:
        # first_chopstick.acquire()
        # second_chopstick.acquire()
        
        # try:
        #     if sushi_count > 0:
        #         sushi_count -= 1
        #         print(f'{name} took a piece! Sushi remaining {sushi_count}')
            
        #     # lets crash the program
        #     if sushi_count == 10:
        #         print(1/0)
        # finally:
        #     second_chopstick.release()
        #     first_chopstick.release()
        
        # another way is to use 
        with first_chopstick:
            with second_chopstick:
                if sushi_count > 0:
                    sushi_count -= 1
                    print(f'{name} took a piece! Sushi remaining {sushi_count}')
                
                if sushi_count == 10:
                    print(1/0)               

if __name__ == '__main__':
    threading.Thread(target=philosopher, args=('Gordon', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=('Alyx', chopstick_b, chopstick_c)).start()
    threading.Thread(target=philosopher, args=('Barny', chopstick_a, chopstick_c)).start() 


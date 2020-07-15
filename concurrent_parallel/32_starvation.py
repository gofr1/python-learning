#!/usr/bin/env python3

import threading

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 5000

def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    sushi_eaten = 0
    while sushi_count > 0:
        with first_chopstick:
            with second_chopstick:
                if sushi_count > 0:
                    sushi_count -= 1
                    sushi_eaten += 1
                    print(f'{name} took a piece! Sushi remaining {sushi_count}')            
    print(f'{name} took {sushi_eaten} pieces')

if __name__ == '__main__':
    for thread in range(50): # lets create 50x3 threads to test starvation
        threading.Thread(target=philosopher, args=(f'Gordon-{thread}', chopstick_a, chopstick_b)).start()
        threading.Thread(target=philosopher, args=(f'Alyx-{thread}', chopstick_a, chopstick_b)).start()
        threading.Thread(target=philosopher, args=(f'Barny-{thread}', chopstick_a, chopstick_b)).start() 
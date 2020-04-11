#!/usr/bin/env python3

import itertools

def main():
    # Infinite counting
    for x in itertools.count(10,5):
        print(x)
        if x == 30:
            break
    
    # Infinite cycling
    x = 0
    w = "RACECAR"
    for c in itertools.cycle(w):
        print(c)
        x += 1
        if x == len(w):
            break
    
    # Infinite repeating
    y = 0
    for r in itertools.repeat(True):
        print(r)
        y += 1
        if y == 4:
            break


if __name__ == '__main__':
    main()
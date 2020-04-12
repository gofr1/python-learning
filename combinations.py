#!/usr/bin/env python3

import itertools

def main():
    # combinations
    # same as permutations but no set will have the same exact elements as another
    # 
    # order doesn't matter
    # you cannot have separate combinations with 
    # the exact same items because then they are the same combination
    coloursForPainting = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]

    for c in itertools.combinations(coloursForPainting, 2): # we want to paint in 2 colours from the list
        print(c) # no same elements in different order
    # 15 combinations
    
    print()

    for c1 in itertools.permutations(coloursForPainting, 2):
        print(c1)
    # 30 (6x5) permutations

if __name__ == '__main__':
    main()
#!/usr/bin/env python3

import itertools

def main():
    # permutations
    # a way, especially oneof several possible variations
    # in which a set of numbers or things can be ordered or
    # arranged
    election = {1: "John", 2: "Tom", 3: "Nathan"}

    for p in itertools.permutations(election):
        print(p) # this will give all possible orderings
    
    for p1 in itertools.permutations(election.values()):
        print(p1)

    for p2 in itertools.permutations(election.values(), 2):
        print(p2) # will give pairs 
        # order does matter, so you will get 
        # same elements in different order

if __name__ == '__main__':
    main()
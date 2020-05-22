#!/usr/bin/env python3

def main():
    # define two lists of numbers
    evens = [r for r in range(1,21) if r%2 == 0]
    odds = [r for r in range(1,21) if r%2 != 0]

    # perform a mapping and filter function on list 
    evenSquared = list(map(lambda e: e**2, evens))
    print(evenSquared)
    
    # same w/filters
    oddSquared = list(map(lambda e: e**2, filter(lambda e: e>3 and e <17, odds)))
    print(oddSquared)

    # derive a new list of numbers from a given list
    evenSquared = [e**2 for e in evens]
    print(evenSquared)

    # limit the items operated on with a predicate condition
    oddSquared = [e**2 for e in odds if e>3 and e<17]
    print(oddSquared)

if __name__ == '__main__':
    main()
#!/usr/bin/env python3

# advanced iteration w/itertools module

import itertools

def testFunc(x):
    return x < 40

def main():
    seq1 = ["Ivan", "John", "Andrew"]

    # cycle iterator over collection
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    
    # accumulate
    vals = [10, 20, 30, 40, 50, 40, 30]
    acc = itertools.accumulate(vals)
    print(list(acc)) # a running addition of values

    acc1 = itertools.accumulate(vals, max)
    print(list(acc1)) #   [10, 20, 30, 40, 50, 50, 50]

    # chain to connect sequences together
    x =itertools.chain("ABCD", "1234")
    print(list(x))
    
    # dropwhile and takewhile will return values until
    # a certain condition is met to stop them
    print(list(itertools.dropwhile(testFunc, vals)))
    print(list(itertools.takewhile(testFunc, vals)))


if __name__ == '__main__':
    main()
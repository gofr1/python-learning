#!/usr/bin/env python3

# double-ended queue
from collections import deque
# you can use it to append/pop data from both sides
import string

def main():
    # initialize a deque with lowercase letters
    d = deque(string.ascii_lowercase)

    # deques support the len() function
    print("Item count:", len(d))

    # deques can be iterated over
    for elem in d:
        print(elem.upper(), end =",")

    # manipulate items from either end 
    print("From the end:", d.pop())
    print("From the beggining:", d.popleft())

    d.append(2) # add to the end
    d.appendleft(1) # add to the beginning

    print(d)

    # rotate the deque
    d.rotate(10) # last 10 items are moved to the beggining
    print(d)


if __name__ == '__main__':
    main()
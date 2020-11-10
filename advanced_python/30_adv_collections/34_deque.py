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
    #* Item count: 26

    # deques can be iterated over
    for elem in d:
        print(elem.upper(), end =",")
    #* A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,

    # manipulate items from either end 
    print("From the end:", d.pop())
    #* From the end: z

    print("From the beggining:", d.popleft())
    #* From the beggining: a
    
    # insert the value in its argument to the right end of deque. 
    d.append(2) # add to the end
    # insert the value in its argument to the left end of deque
    d.appendleft(1) # add to the beginning

    print(d)
    #* deque([1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 2])
    # rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to left. 
    # Else rotation is to right
    d.rotate(10) # last 10 items are moved to the beggining
    print(d)
    #* deque(['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 2, 1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])

    d = deque([1,2,3,4,5])
    # add multiple values at the left end of deque
    d.extendleft([0])
    # add multiple values at the right end of deque
    d.extend([6,7,8])
    print(d)
    #* deque([0, 1, 2, 3, 4, 5, 6, 7, 8])

    #  reverse order of deque elements
    d.reverse()
    print(d)
    #* deque([8, 7, 6, 5, 4, 3, 2, 1, 0])

if __name__ == '__main__':
    main()
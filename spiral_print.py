#!/usr/bin/env python3

from math import sqrt 

def main():
    number = 36
    length = int(sqrt(number))

    listOfNumbers = list() 
    for _ in range(length):
        listOfNumbers.append(list([0]*length))
    
    avgLength = length//2 if length%2 != 0 else length//2 - 1

    x = avgLength
    y = avgLength
    turnNumber = 0
    t = 0
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    turns = list()
       
    for n in range(1,length+1):
        turns.append(n)
        turns.append(n)
    
    if length%2 == 0:
        l = len(turns)
        turns[l-1] -= 1
        turns[l-2] -= 1

    for el in range(1,number+1):
        listOfNumbers[x][y] = el

        if turnNumber > 1:
            x, y = x + xx, y + yy
            turnNumber -= 1
        else:
            turnNumber = turns[t]
            xx, yy = directions.pop()
            x, y = x + xx, y + yy
            directions.insert(0, (xx, yy))
            t += 1
        
    for n in range(len(listOfNumbers)):
        print(listOfNumbers[n])

if __name__ == '__main__':
    main()
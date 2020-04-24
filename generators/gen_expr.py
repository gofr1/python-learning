#!/usr/bin/env python3

def main():
    # list comprehension example
    # newList = [item.upper() for item in collection]
    evenIntList = [n for n in range(10) if n%2 == 0]
    print(evenIntList)

    # generator expression
    # (item.upper() for item in collection)
    evenIntGenExp = (n for n in range(10) if n%2 == 0)
    print(evenIntGenExp)
    print(list(evenIntGenExp))

if __name__ == '__main__':
    main()
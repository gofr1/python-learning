#!/usr/bin/env python3

from enum import Enum, unique, auto

# @unique
# class Fruit1(Enum):
#     APPLE = 1
#     BANANA = 2
#     ORANGE = 3
#     TOMATO = 4
#     PEAR = 1 # ValueError hear because of duplicate values

class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()
    # no duplicate keys
    # but it is ok to have duplicate values

def main():
    # enums have human-readable values ant types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # enums have name a nd value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # print auto-generated values
    print(Fruit.PEAR.value)

    # enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "I'm banana man"
    print(myFruits[Fruit.BANANA])

if __name__ == '__main__':
    main()
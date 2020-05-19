#!/usr/bin/env python3

import collections

def main():
    # create a nemedtuple
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10,20)
    p2 = Point(20,30)

    print(p1, p2)
    print(p1.x, p2.y)

    # use _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1)

if __name__ == '__main__':
    main()
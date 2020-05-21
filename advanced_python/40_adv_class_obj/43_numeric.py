#!/usr/bin/env python3

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return '<Point x:{0},y:{1}>'.format(self.x, self.y)

    # implement addition
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    # implement substraction
    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)


    # implement in-place addition
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


def main():
    # declare some points
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)

    # add two points
    p3 = p1+p2
    print(p3)

    # substract two points
    p4 = p2-p1
    print(p4)

    # perform in-place addition
    p1 += p2
    print(p1)

if __name__ == '__main__':
    main()
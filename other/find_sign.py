#!/usr/bin/env python3

def find_sign(x):
    # a tuple has index 0 and 1
    # that you get from boolean x < 0
    return x and (1, -1)[x < 0]

def tricky_sign(x):
    return (x > 0) - (x < 0)

find_sign(42) #*1
find_sign(0) #*0
find_sign(-2.0) #*-1

tricky_sign(42) #*1
tricky_sign(0) #*0
tricky_sign(-2.0) #*-1
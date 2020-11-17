#!/usr/bin/env python3

from math import e

def find_e(n):
    e = 1
    factorial = 1
    for i in range(1,n):
        factorial *= i
        e += 1 / factorial
    return e

find_e(18) #* 2.7182818284590455
e          #* 2.718281828459045
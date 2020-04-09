#!/usr/bin/env python3

import math

def main():
    # Ceiling and Floor
    cookies = 10.3
    candy = 7
    print(math.ceil(cookies))
    print(math.ceil(candy))

    age = 47.9
    otherAge = 47
    print(math.floor(age))
    print(math.floor(otherAge))
    
    # Factorial and Square root
    print(math.factorial(10))
    print(math.sqrt(64)) # returns float

    # Greatest Common Denominator (GCD)
    # 8/52 -> 2/13 because both parts can be divided by 4
    print(math.gcd(52, 8))
    print(math.gcd(8, 52))

    # Degrees & Radians
    # degrees 0 -> 360
    # radians 0 -> 2pi
    rad = math.pi * 2
    print(math.radians(360)) # 2pi
    print(math.degrees(rad)) # returns float

if __name__ == '__main__':
    main()
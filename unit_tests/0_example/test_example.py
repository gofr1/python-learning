#!/usr/bin/env python3

# sudo pip3 install pytest

# Use cases:
# 0. Can I call FizzBuzz
# 1. Get "1" when I pass in 1 
# 2. Get "2" when I pass in 2
# 3. Get "Fizz" when I pass in 3
# 4. Get "Buzz" when I pass in 5
# 5. Get "Fizz" when I pass in 6 (a multiple of 3)
# 6. Get "Buzz" when I pass in 10 (a multiple of 5)
# 7. Get "FizzBuzz" when I pass in 15 (a multiple of 3 and 5)

import pytest

def fizzBuzz(value):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return 'FizzBuzz'
        return 'Fizz'
    if isMultiple(value, 5):
        return 'Buzz'
    return str(value)


def isMultiple(value, mod):
    return (value % mod) == 0

# 0
def test_canCallFizzBuzz():
    fizzBuzz(1)

# lets generalize 1 and 2 use cases check
def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal

# 1 
def test_returns1With1PassedIn():
    checkFizzBuzz(1, '1')

#2
def test_returns2With2PassedIn():
    checkFizzBuzz(2, '2')

# 3
def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, 'Fizz')

# 4
def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5, 'Buzz')

# 5
def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6, 'Fizz')

# 6
def test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10, 'Buzz')

# 7
def test_returnsFizzBuzzWith15PassedIn():
    checkFizzBuzz(15, 'FizzBuzz')
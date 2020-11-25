#!/usr/bin/env python3

# An assertion is a sanity check to make sure your code isn’t doing something obviously wrong.
# Assertions are for programmer errors, not user errors. 

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
ages
#* [73, 47, 80, 17, 15, 22, 54, 92, 57, 26]
assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.

#* Traceback (most recent call last):
#*   File "<stdin>", line 1, in <module>
#* AssertionError

#! Unlike exceptions, your code should not handle assert statements 
#! with try and except; if an assert fails, your program should crash.
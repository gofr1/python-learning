#!/usr/bin/env python3
#
# {} in print statement is called placeholder
strX = "is here"
intX = 42

# in python 2
print("Some text %s and %d" % (strX, intX))

# in python 3
print("Some text {} and {}".format(strX, intX))

# in python 3.6 fstrings were introduced
print(f"Some text {strX} and {intX}") # f stands for format


x = ('a','b','c')
print("{}, {}, {}".format(*x))
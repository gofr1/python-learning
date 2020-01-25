import sys

names = []

print(sys.getrefcount(names))

# reference counter

import keyword
print(keyword.kwlist) # list of python keywords

dir(__builtins__) # built-in functions

# variables should:
# be lowercase
# use _ as delimeter
# not use any built-in function names

# if you are not sure take a look at PEP8
# Python Enhancement Proposal

# task1
import math

p = math.pi
r = 10

s = p * (r**2)
print(s)

# task2
b = 10
h = 2

p = 2*(b+h)
print(p)

# object identity

name = "Ilia"
id(name)
first = name
id(first)
print(first is name)

name = 'Vasya'
some_var = "Vasya"
print(name is some_var)
id(name)
id(some_var)

# object type
name = "Ilia"
type(name)

# lists and dictionaries are mutable 
# they dont change the oblect id
names = []
id(names)

names.append("Fred")
id(names)

# all other types are immutable (they are created with new id and all value is deleted)
int_var = 1000
id(int_var)
int_var = int_var +1
id(int_var)

dir() # show the list of available variables in current file

# task1
a = 10.0
id(a)
a = a +20
id(a)
print(a)

#task2
digits = []
id(digits)
type(digits)
print(digits)

digits.append(300)
id(digits)
type(digits) # list
print(digits)
type(digits[0]) # integer
print(digits[0]) 

digits.append('300')
id(digits)
type(digits) # list
print(digits)
type(digits[1]) # str
print(digits[1]) 
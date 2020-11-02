#!/usr/bin/env python3

# Map applies a function to all the items
# old way
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
print(squared)

# Map way
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

# Instead of a list of inputs we can even have a list of functions
def mult(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [mult, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Filter creates a list of elements for which a function returns true
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Reduce is a function for performing some computation on a list and returning the result.
# It applies a rolling computation to sequential pairs of values in a list.
# old way
vl = 1
lst = [1, 2, 3, 4]
for num in lst:
    vl = vl * num
print(vl)

from functools import reduce
vl = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(vl)

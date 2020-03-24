#!/usr/bin/env python3
# 
# interesting problem
x = .1 + .1 + .1 - 0.3
print(x)
# 5.551115123125783e-17

# This is the difference between accuracy and precision
# Because of the way that the computers do floating point
# the're sacrifice accuracy for precision and so it may
# do this arithmetic correctly to 17 decimal places
# which is the precision of the floating point processor
#
# workaround

import decimal

a = decimal.Decimal('.1') # string is used because if we path float value
b = decimal.Decimal('.3') # we will lost accuracy
x = a + a + a - b
print(x)
print(type(x))
# 0.0
# <class 'decimal.Decimal'>
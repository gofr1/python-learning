#!/usr/bin/env python3
#
# Conditional operators:
#
# Comparison operators
# == equal
# != not equal (<> - cant be used but x != 0 is the same as x > 0 and x < 0
# <  less than
# >  greater than
# <= less than or equal
# >= greater than or equal
# 
# Logical operators
# and  True if both x and y
# or   True if x or y
# not  invert state
# 
# Identity operator
# x is y      True if the same object
# x is not y  True if not the same object
# 
# Membership operator
# x in y      True if x is a member of collection y
# x in not y  True if x is not a member of collection y

if True:
    print('1')
elif False:
    print('2')
else:
    print('3')
# 1

# if nothing is evaluated as True else block will be executed
if False:
    print('1')
elif False:
    print('2')
else:
    print('3')
# 3

# the first condition that evaluates as True will be executed
if False:
    print('1')
elif False:
    print('2')
elif True:
    print('3')
elif True:
    print('4')
else:
    print('5')
# 3

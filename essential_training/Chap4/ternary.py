#!/usr/bin/env python3
#
# From python 2.5 Python includes a ternary conditional operator

def bear_state(hungry):
    x = 'Feed the bear now' if hungry else 'Do not feed the bear' # ternary 
    return x

hungry = True
print(bear_state(hungry))
# Feed the bear now

hungry = False
print(bear_state(hungry))
# Do not feed the bear
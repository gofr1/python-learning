#!/usr/bin/env python3
# 
# A statement is a unit of execution
# An expression is a unit of evaluation
#
# In python, an expression is any combination
# of literals, identifiers and operators
# Generally everything that returns a value 
# is an expression
#
# A statement is a line of code

import platform

version = platform.python_version()

print('This is python version {}'.format(version)); print('hello') # ; possible but extremely rare
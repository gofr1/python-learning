#!/usr/bin/env python3

# and    And
# or     Or
# not    Not
# in     Value in set
# not in Values not in set
# is     Same object identity
# not is Not same object identity

a = True
b = False

x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false')

if not b:
    print('expression is true')
else:
    print('expression is false')

if not a:
    print('expression is true')
else:
    print('expression is false')

if y in x:
    print('expression is true')
else:
    print('expression is false')
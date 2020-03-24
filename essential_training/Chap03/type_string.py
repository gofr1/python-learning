#!/usr/bin/env python3
# 
# Python uses a form of dynamic typing
# sometimes called duck typing where the
# type of a value is determined by the value itself

x = 7
y = 7.0
z = '7.0'
q = True
n = None

print('x is {} {}'.format(x, type(x)))
print('y is {} {}'.format(y, type(y)))
print('z is {} {}'.format(z, type(z)))
print('q is {} {}'.format(q, type(q)))
print('n is {} {}'.format(n, type(n)))

# you can set the order of format arguments 
# by pitting 0, 1 etc in placeholders
'some beautiful string {1} {0}'.format('here', 'is') 

print('lets add some spaces to make the data look fine\n\n|{0:^6}|{1:^6}|\n|{2:<6}|{3:>6}|'.format('name', 'year', 'John', 1990))
# lets add some spaces to make the data look fine
# 
# | name | year |
# |John  |  1990|
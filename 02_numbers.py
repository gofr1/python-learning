type(1) #int

type(2.0) #float

# for float standart IEEE 454 is used
# if you need more accuracy - you need to use 'decimal' module (slow)

2+6
#print(_) # _ is variable that stores the last result

.4 + .01 # accuracy is bad
6 + .2 # int + float = float

print('num: %s %d' % (1, 2))
'some text ' * 2 # will print 2 times concatenated string

4//3
4/3

2/3
2%3 # dont use modulo with negative numbers

10.3 ** 3 # power operator

# you can use 'operator' module for math operations

import operator
operator.add(2,4)
2+4

# task1

sleep = [6.2, 7, 8, 5, 6.5, 7.1, 8.5] # list
s = 0
i = 0
for sl in sleep:
    s += sl
    i += 1

print('days of sleep: %i, total sleep: %s, avg: %a' % (i, s, s/i))

#!/usr/bin/env python3
#! O(1)
# Constant time
# Many simple checks and assignments

my_fav_desserts = {'cheesecake': 1, 'cookie': 2}
print(my_fav_desserts['cheesecake'])

#! O(n)
# Linear time
# Simple for loops are almost always O(n)
my_fav_desserts = ['cheesecake', 'cookie', 'cake']
for dessert in my_fav_desserts:
    print(dessert)

#! O(log n)
#
# Binary search is O(log n) in the worst case because each time
# you eliminate options, you eliminate half of them

#! O(n^2)
# Two nested for loops 
my_fav_desserts = ['cheesecake', 'cookie', 'cake']
quantities = [5, 10, 20]
for dessert in my_fav_desserts:
    for qty in quantities:
        print(f'{dessert}: {qty}')


# Simple visualization of Big-O Compexity
from math import factorial, log
import matplotlib.pyplot as plt

x = range(1,101)

y1 = [1]*100
yn = range(100)
ylogn = [log(x) for x in x]
yn2 = [x**2 for x in x]
ynlogn = [x*log(x) for x in x]
y2n = [2**x for x in x]
ynn = [factorial(x) for x in x]

x_limit = max(x)

plt.plot(y1, label='O(1)')
plt.plot(ylogn, label='O(log(n))')
plt.plot(yn, label='O(n)')
plt.plot(ynlogn, label='O(n*log(n))')
plt.plot(yn2, label='O(n^2)')
plt.plot(y2n, label='O(2^n)')
plt.plot(ynn, label='O(n!)')

ax = plt.gca()
ax.legend(['O(1)', 'O(log(n))', 'O(n)', 'O(n*log(n))', 'O(n^2)', 'O(2^n)', 'O(n!)']) 
ax.set_ylim(0, 1000)
ax.set_xlim(0, x_limit)

plt.rc('grid', linestyle=':', color='blue', linewidth=0.5)
plt.yticks(range(0, 1000, 100))
plt.xticks(range(0, x_limit, 10))

# setting the title using Matplotlib
plt.title('Big-O Complexity')
plt.grid(True)

plt.show()
# task1
# import module from file
import sys
sys.path.append('~/Documents/python_learning/packages')

from begin import prime

prime(44)

sys.path.pop()

# task2
# import package from directory
sys.path.append('~/Documents/python_learning/packages')

import utils

prime(7)
prime(44)

sys.path.pop()
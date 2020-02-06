3/0

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero

def err():
    1/0

def start():
    return middle()

def middle():
    return more()

def more():
    err()

start()

# that will show:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in start
#   File "<stdin>", line 2, in middle
#   File "<stdin>", line 2, in more
#   File "<stdin>", line 2, in err
# ZeroDivisionError: division by zero
# all the chain of calls with error

# two styles of error handling:
# LBYL - Look Before You Leap
# e.g.

numerator = 10
divisor = 0

if divisor != 0:
    result = numerator / divisor
else:
    result = None

result

# EAFP - Easier to Ask for Forgiveness than Permission
# if operation failed it would be intercepted in except block
# e.g.

numerator = 10
divisor = 0

try:
    result = numerator / divisor
except ZeroDivisionError as e:
    result = None

result

# 1. handle only those errors, which are expected
# 2. don't supress exceptions that you cannot handle
# 3. use global handlers

# while 1:
#     try:
#         result = process_input()
#     except Exception as e:
#         log_error(e)

# to handle various exceptions in different ways
# you can use few except blocks or except (EceptionTypes,...)

# after reaching one of the except blocks
# next blocks are not used

# finally
# runs always even if there was exceptions

numerator = 10
divisor = 0

try:
    result = numerator / divisor
except ZeroDivisionError as e:
    result = None
finally:
    runs_anyway = 'Hi'

result
runs_anyway

# finally is usualy used to close opened files
# releasing some resources

try:
    print('Hi!')
except Exception as e:
    print('Error')
else: # it will be executed if no exceptions occured
    print('Success')
finally:
    print('at last')


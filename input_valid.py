#!/usr/bin/env python3

# Srandard way
while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    break

print(f'Your age is {age}.')


# PyInputPlus contains functions similar to input() for several kinds of data: 
# numbers, dates, email addresses, and more. 
# If the user ever enters invalid input, such as a badly formatted date or a number 
# that is outside of an intended range, PyInputPlus will reprompt them for 
# input just like our code in the previous section did.

# sudo pip3 install pyinputplus
import pyinputplus as pyip

response = pyip.inputNum()
#* k
#* 'k' is not a number.
#* 89

response = pyip.inputInt(prompt = 'Enter a number: ')

# The min, max, greaterThan, and lessThan keyword arguments
response = pyip.inputNum('Enter num: ', min = 4)
#* Enter num: 2
#* Number must be at minimum 4.
#* Enter num: 24

response = pyip.inputNum('Enter num: ', greaterThan = 4)
#* Enter num: 4
#* Number must be greater than 4.
#* Enter num: 6

response = pyip.inputNum('>', min=4, lessThan=6)
#* >2
#* Number must be at minimum 4.
#* 7
#* Number must be less than 6.
#* >5

# The limit, timeout, and default keyword arguments
response = pyip.inputNum(limit = 2)
#* ...
#* pyinputplus.RetryLimitException

response = pyip.inputNum(timeout = 5)
# if nothing is prompt in 5 seconds
#* ...
#* pyinputplus.TimeoutException

response = pyip.inputNum(limit = 2, default = 'N/A')
#* ff
#* 'ff' is not a number.
#* gg
#* 'gg' is not a number.

print(response)
#* N/A
#!/usr/bin/env python3

listOfStr = ['hi', 'this', 'is', 'a', 'message', 'to', 'you']
# Get string with max value in list of string based on alphabetical
maxVal = max(listOfStr)
print(maxVal)
#* you

# Get the string with maximum size in this list of string
maxVal = max(listOfStr, key=lambda x: len(x))
print(maxVal)
#* message

# Find item in a dictionary with maximum value
sampleDict = {'John': 4, 'Jane': 23, 'Jack': 11, 'Andrew': 16, 'Mark': 20}
maxVal = max(sampleDict.items(), key=lambda x: x[1])
print(maxVal)
#* ('Jane', 23)


# all() function returns True if all items in an iterable are true, otherwise it returns False.
sampleList = [0, 1, 1]
x = all(sampleList)
print(x)
#* False

# For dictionaries the all() function checks the keys, not the values.
sampleDict = {0 : "Apple", 1 : "Orange"}
x = all(sampleDict)
print(x)
#* False

# Test if all numbers in the list are positive
listOfNumbers = [1, 2, 3, 8, 10]
if all(x > 0 for x in listOfNumbers):
    print('All positive')
else:
    print('Not all are positive')
#* All positive

# Unzip!
someData = [(1, 'abc'), (2, 'def'), (3, 'ghi')]

numbers, letters = zip(*someData)
print(numbers)
#* (1, 2, 3)
print(letters)
#* ('abc', 'def', 'ghi')
print(type(numbers))
#* <class 'tuple'>

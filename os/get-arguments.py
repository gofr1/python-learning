#!/usr/bin/env python3

from sys import argv


arguments = argv
print(str(arguments))
print(arguments[0])
print(arguments[1])
print(arguments[2])
print(str(arguments[1:]))

# from bash run 
# python3 get-arguments.py apple banana cherry

#* ['get-arguments.py', 'apple', 'banana', 'cherry']
#* get-arguments.py
#* apple
#* banana
#* ['apple', 'banana', 'cherry']

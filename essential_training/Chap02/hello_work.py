#!/usr/bin/env python3
# Shebang line
import platform as p 

def main(): # function declaration/definition
    message() # function call

def message():
    print('This is python version {}'.format(p.python_version())) # indented to this function level
    if True: # condition
        print('True') # intended to if block
        # block is the statements within some statement
# Function, objects and modules do define scope

if __name__ == '__main__':
    main()
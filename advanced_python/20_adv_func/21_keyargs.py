#!/usr/bin/env python3

def myFunction(arg1, arg2, *, supressExceptions=False):
    pass

def main():
    # try to call function w/o the keyword
    # myFunction(1, 2, True) # this will return error: 
    # TypeError: myFunction() takes 2 positional arguments but 3 were give
    
    myFunction(1, 2, supressExceptions=True)

if __name__ == '__main__':
    main()
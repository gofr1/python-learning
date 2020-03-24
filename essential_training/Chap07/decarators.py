#!/usr/bin/env python3

# decorator
# is a form of metaprogramming and it can 
# be described as a special type of function
# that returns a wrapper function

def f1():
    print('this is f1')

x = f1
x() # this is f1

def f2():
    def f3(): # you can not call this function directly
        print('this is f3')
    return f3

x = f2()
x() # this is f3

def f4(f):
    def f5():
        print('this is before the function call')
        f()
        print('this is after the function call')
    return f5

@f4 # it is a decorator
def f6():
    print('this is f6')

f6()
# x = f4(f6)
# x()
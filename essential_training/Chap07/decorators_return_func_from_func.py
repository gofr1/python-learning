#!/usr/bin/env python3

#! Returning functions from within functions
def say_hi(name = 'Jack'):

    def greet():
        return 'Now you are in the greet() function'

    def welcome():
        return 'Now you are in the welcome() function'

    if name == 'Jack':
        return greet
    else:
        return welcome

a = say_hi()
print(a)
#* <function say_hi.<locals>.greet at 0x7fad98cb20d0>
# This clearly shows that `a` now points to the greet( function in say_hi()

# Now try this
print(a())
#* Now you are in the greet() function


# In the if/else clause we are returning greet and welcome, not greet() and welcome(). 
# Why is that? It’s because when you put a pair of parentheses after it, the function gets executed,
# whereas if you don’t put parenthesis after it, then it can be passed around and can be 
# assigned to other variables without executing it.

say_hi()()
#* Now you are in the greet() function

say_hi('John')()
#* 'Now you are in the welcome() function'
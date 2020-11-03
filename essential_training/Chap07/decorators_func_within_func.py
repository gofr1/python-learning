#!/usr/bin/env python3

#! Defining functions within functions
def say_hi(name = 'Jack'):
    print("now you are inside the say_hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the say_hi() function")

say_hi()
#* now you are inside the say_hi() function
#* now you are in the greet() function
#* now you are in the welcome() function
#* now you are back in the say_hi() function

# This shows that whenever you call say_hi(), greet() and welcome()
# are also called. However the greet() and welcome() functions
# are not available outside the say_hi() function e.g:

greet()
#* NameError: name 'greet' is not defined
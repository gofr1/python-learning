#!/usr/bin/env python3

#! decorator
# is a form of metaprogramming and it can 
# be described as a special type of function
# that returns a wrapper function
#! or you can say they are functions which modify the functionality of other functions. 

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

# lets define a function
def say_hi(name = 'Jack'):
    return f'Hi {name}'

print(say_hi())
#* Hi Jack

# We can even assign a function to a variable like
greet = say_hi
# We are not using parentheses here because we are not calling the function say_hi
# instead we are just putting it into the greet variable. Let's try to run this

print(greet())
#* Hi Jack

# Let's see what happens if we delete the old hi function!
del say_hi
print(say_hi())
#* NameError: name 'say_hi' is not defined

print(greet())
#* Hi Jack

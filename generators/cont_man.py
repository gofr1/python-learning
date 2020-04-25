#!/usr/bin/env python3

# Context managers:
# - control structure
# - used after "with"
# - setup
# - yield control
# - wrap-up

# a pythin object that is able to act as a control
# structure when used after "with" statement
# must make "enter" and "exit"

# # basic syntax
# @contextmanager
# def simple_context_manager(obj):
#     try:
#         # do something
#         yield
#     finally:
#         # wrap-up

from contextlib import contextmanager

@contextmanager # decorator
def simple_context_manager(obj):
    try:
        obj.some_property += 1 # increment some_property
        yield # give control back to color
    finally:
        obj.some_property -= 1 # decrement some_property back

class SomeObj(object):
    def __init__ (self, arg):
        self.some_property = arg
    
    def __str__ (self):
        return f'Some property value is: {self.some_property}'

def main():
    obj = SomeObj(5)
    print(obj)

    with simple_context_manager(obj):
        print(obj)
    
    print(obj)

if __name__ == '__main__':
    main()
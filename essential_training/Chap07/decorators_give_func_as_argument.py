#!/usr/bin/env python3

#! Giving a function as an argument to another function
def say_hi():
    return 'Hi Jack'

def do_soomething_before(func):
    print(f'Doing some stuff before {func.__name__}!')
    print(func())

do_soomething_before(say_hi)
#* Doing some stuff before say_hi!
#* Hi Jack
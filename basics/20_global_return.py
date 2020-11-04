#!/usr/bin/env python3

# get result with the help of global variable
def add(value1, value2):
    global result
    result = value1 + value2

add(4, 5)
print(result)
#* 9

# get multiple results
def get_info():
    global name
    global age
    name = 'John'
    age = 25

get_info()

print(name)
#* John
print(age)
#* 25

# This is not commonly used approach, don't use it in production
# It's just for the sake of demonstration

# better use return:

def get_info_return():
    name = 'John'
    age = 25
    return (name, age)

info = get_info_return()
print(info[0])
#* John
print(info[1])
#* 25

# or
name, age = get_info_return()
print(name)
#* John
print(age)
#* 25
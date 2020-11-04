#!/usr/bin/env python3
 
from collections import namedtuple

def get_info():
    Person = namedtuple('Person', 'name age')
    return Person(name = 'John', age = 25)

# Use as namedtuple
person = get_info()
print(person, type(person))
#* Person(name='John', age=25) <class '__main__.Person'>
print(person.name)
#* John
print(person.age)
#* 25

# Unpack it immediately
name, age = get_info()
print(name)
#* John
print(age)
#* 25
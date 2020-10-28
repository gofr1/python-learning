#!/usr/local/bin/python3.9

import sys

v = sys.version_info
print('Python version {}.{}.{}'.format(*v))

# Dictionary Merge & Update
# Merge (|) and update (|=) operators
x = {"one": 1, "two": 2}
y = {"three": 3, "four": 4}
z = {"five": 5}

x|y
#* {'one': 1, 'two': 2, 'three': 3, 'four': 4}
y|x
#* {'three': 3, 'four': 4, 'one': 1, 'two': 2}

z |= x
z
#* {'five': 5, 'one': 1, 'two': 2}
z |= y
z
#* {'five': 5, 'one': 1, 'two': 2, 'three': 3, 'four': 4}

# New String Methods to Remove Prefixes and Suffixes
smth = 'SomeThing'

smth.removeprefix('Some')
#* 'Thing'

smth.removesuffix('Thing')
#* 'Some'

# Type Hinting Generics in Standard Collections
def greet_all(names: list[str]) -> None: # we can declare that we need list of string f.e.
    for name in names:
        print("Hello", name)

greet_all(['John', 'Gwen'])
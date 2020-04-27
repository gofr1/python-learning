#!/usr/bin/env python3

# coroutines
# receive values/input (repeatedly)
# process values
# may not return anything
# not for iteration
# 
# Fumction vs Coroutine
# It's the same function each time you call it
# Persistent properties can be changed and altered

# yield in coroutines:
# pauses flow
# captures sent values

# is a generator with send() method

def coroutine_example():
    while True:
        x = yield
        # do something with x
        print(x)

def main():
    c = coroutine_example()
    next(c)
    c.send(10)
    c.close()

if __name__ == '__main__':
    main()
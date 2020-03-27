#!/usr/bin/env python3

class Foo:
    def __init__(self, bar):
        self._bar = bar
    
    def __repr__(self):
        return f'repr: the message is "{self._bar}" \U0001F596'

    # if you don't have __str__ method in your class
    # printing object will provide __repr__ version
    def __str__(self):
        return f'str: he message is "{self._bar}" \U0001F596'

def main():
    h = 'Hello, World!'
    print(repr(h)) # representation

    f = Foo(h)
    print(repr(f)) 
    print(f)
    # this will give <__main__.Foo object at 0x...>
    # so we can change __repr__ method of a class
    
    # almost same as repr, but will print unicode characters in code representation
    print(ascii(f))
    
    # ord and chr functions help to work with unicode
    print(ord('\N{Raised hand with part between middle and ring fingers}'))
    print(ord('\U0001F596'))
    print(chr(128406))

if __name__ == '__main__':
    main()
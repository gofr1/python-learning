#!/usr/bin/env python3

class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'pit bull'
        self._name = kwargs['name'] if 'name' in kwargs else 'Thunder'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'woof'
    
    # as we path some variable into this method it becomes setter
    # so now they are getter setter methods
    def type(self, t = None):
        if t: self._type = t
        return self._type
    
    def name(self, n = None):
        if n: self._name = n
        return self._name
    
    def sound(self, s = None):
        if s: self._sound = s
        return self._sound
    
    # specially-named method which provides the string representation of an object
    def __str__(self):
        return f'The {self.type()} is named {self.name()} and says {self.sound()} '
    
def main():
    a0 = Animal(type = 'kitten', name = 'Fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'Donald', sound = 'quack')
    print(a0) # __str__ is used here
    print(a1)

    # use a setter
    a0.sound('meow')

    print(a0)
    print(Animal(type = 'velociraptor', name = 'Veronica', sound = 'hello'))
    print(Animal())

if __name__ == '__main__':
    main()
    
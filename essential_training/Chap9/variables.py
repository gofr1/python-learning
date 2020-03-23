#!/usr/bin/env python3

class Animal:
    # this is class variable
    x = [1, 2, 3]

    def __init__(self, **kwargs):
        # this are object variables
        # they exists only when object is created from the class
        # they do not exists in the class itself
        self._type = kwargs['type'] if 'type' in kwargs else 'pit bull'
        self._name = kwargs['name'] if 'name' in kwargs else 'Thunder'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'woof'
    
    def type(self, t = None):
        if t: self._type = t
        return self._type
    
    def name(self, n = None):
        if n: self._name = n
        return self._name
    
    def sound(self, s = None):
        if s: self._sound = s
        return self._sound
    
    def __str__(self):
        return f'The {self.type()} is named {self.name()} and says {self.sound()} '
    
def main():
    a0 = Animal(type = 'kitten', name = 'Fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'Donald', sound = 'quack')
    print(a0)
    print(a1)
    # object variables could be changed
    # but it is bad practice
    a0._name = 'Johh'
    print(a0)

    # class variable could be changed
    # but it will change for all instances of a class
    # bad idea to use that
    print(a0.x)
    a1.x[0] = 7
    print(a0.x)

if __name__ == '__main__':
    main()
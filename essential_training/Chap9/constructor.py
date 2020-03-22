#!/usr/bin/env python3

class Animal:
    # def __init__(self, type, name, sound): # this is initializer or constructor
    #     # discourage users of the object from accessing these variables directly
    #     self._type = type
    #     self._name = name
    #     self._sound = sound
    
    # another way with key word arguments and defaults
    def __init__(self, **kwargs):
        # _ in variable name indicates that this is private variable
        self._type = kwargs['type'] if 'type' in kwargs else 'pit bull'
        self._name = kwargs['name'] if 'name' in kwargs else 'Thunder'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'woof'
    
    # getters or accessors
    def type(self):
        return self._type
    
    def name(self):
        return self._name
    
    def sound(self):
        return self._sound
    
def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named {} and says "{}"'.format(o.type(), o.name(), o.sound()))

# def main():
#     a0 = Animal('kitten', 'fluffy', 'rwar')
#     a1 = Animal('duck', 'donald', 'quack')
#     print_animal(a0)
#     print_animal(a1)
#     print_animal(Animal('velociraptor', 'veronica', 'hello'))

def main():
    a0 = Animal(type = 'kitten', name = 'Fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'Donald', sound = 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(type = 'velociraptor', name = 'Veronica', sound = 'hello'))
    print_animal(Animal())

if __name__ == '__main__':
    main()
    
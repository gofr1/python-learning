#!/usr/bin/env python3


class Person():
    def __init__(self):
        self.fname = "John"
        self.lname = "Wick"
        self.age = 50
    
    def __repr__(self): # overrides all
        return '<Person Class - fname: {0}, lname: {1}, age: {2}>'.format(self.fname, self.lname, self.age)

    def __str__(self):
        return 'Person ({0} {1} is {2})'.format(self.fname, self.lname, self.age)  
    
    # let's change butes
    def __bytes__(self):
        val = 'Person:{0}:{1}:{2})'.format(self.fname, self.lname, self.age)  
        return bytes(val.encode('utf-8'))

def main():
    # create a new Person object
    cls1 = Person()

    # use different functions to convert it to string
    print(repr(cls1))
    print(str(cls1))
    print("{}".format(cls1))

    # check bytes
    print(bytes(cls1))

if __name__ == '__main__':
    main()
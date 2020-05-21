#!/usr/bin/env python3

class myColour():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100
    
    # use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == 'rgbcolour':
            return (self.red, self.green, self.blue)
        elif attr == 'hexcolour':
            return '#{0:02x}{1:02x}{2:02x}'.format(self.red, self.green, self.blue)
        else:
            raise AttributeError

    # use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == 'rgbcolour':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val) # if you don't mention this super method
            # getattr will be called on initiation of a class


    # use dir to list the available properties
    def __dir__(self):
        return ('red', 'green', 'blue', 'rgbcolour', 'hexcolour')


def main():
    # create an instance of myColour
    cls1 = myColour()

    # print the value of a computed attribute
    print(cls1.rgbcolour)
    print(cls1.hexcolour)

    # set the value of a computed attribute
    cls1.rgbcolour = (125, 200, 86)
    print(cls1.rgbcolour)
    print(cls1.hexcolour)

    # access a regular attribute
    print(cls1.red)

    # list the available attributes
    print(dir(cls1))


if __name__ == '__main__':
    main()
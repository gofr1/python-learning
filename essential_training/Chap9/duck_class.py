#!/usr/bin/env python3

# class definition
class Duck:
    # class variables
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'
    
    # methods
    def quack(self):
        print(self.sound)
    
    def move(self):
        print(self.movement)

def main():
    donald = Duck()
    donald.quack() # invoke the object method
    donald.move()

if __name__ == '__main__':
    main()
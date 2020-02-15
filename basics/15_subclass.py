class CorrectChair: 
    ''' A Chair on a chairlift '''
    max_occupants = 4

    def __init__(self, id):
        self.id = id
        self.count = 0
    
    def load(self, number):
        new_val = self._check(self.count + number)
        self.count = new_val
    
    def unload(self, number):
        new_val = self._check(self.count - number)
        self.count = new_val
    
    def _check(self, number): # private method is defined
        if number < 0 or number > self.max_occupants:
            raise ValueError('Invalid count:{}'.format(number))
        return number

# this is subclass
# parent is CorrectChair class (or it is called superclass)
class Chair6(CorrectChair):
    max_occupants = 6

Chair6.__bases__
#(<class '__main__.CorrectChair'>,)
# __bases__ attribute for subclass will show main class

class StallChair(CorrectChair):
    def __init__(self, id, is_stalled):
        super().__init__(id)
        self.is_stalled = is_stalled
        self.stalls = 0
    
    def load(self, number):
        if self.is_stalled(number, self):
            self.stalls += 1
        super().load(number)

import random
def ten_percent(number, chair):
    return random.random() < .1

stall42 = StallChair(42, ten_percent)


stall42.unload(2)
stall42.load(2)
stall42.stalls


# task1
# cat

class Cat:
    '''This is a cat'''
    # what cat can do?
    # what properties doed it has?
    # create a tiger subclass
    def __init__(self, name):
        self.name = name
        self.is_sleeping = False
        self.is_hungry = False

    def sleep(self): 
        self.is_sleeping = True if self.is_sleeping == False else False

    def eat(self):
        self.is_hungry = False if self.is_hungry == True else True
    
    def pur(self):
        print('Puuur!')

my_cat = Cat("Simon")

my_cat.name
my_cat.is_sleeping
my_cat.is_hungry
my_cat.pur()

my_cat.sleep()
my_cat.is_sleeping

class Tiger(Cat):
    def pur(self):
        print("Roaaarrr!!!")

my_tiger = Tiger("Sherhan")
my_tiger.pur()

# task2


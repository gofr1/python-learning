#!/usr/bin/env python3

import sys
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    # This class inherits from Abstract Base Classto allow
    # the use of the @abstractmethod decorator

    def template_method(self):
        '''This is the template method that contains a collection of 
        methods to stay the same, to be overriden, and to be overriden optionally.'''
        self.__always_do_this()
        self.do_step_1()
        self.do_step_2()
        self.do_this_or()

    def __always_do_this(self):
        # this is a protected method that should not be overriden
        name = sys._getframe().f_code.co_name
        print(f'{self.__class__.__name__}.{name}')
    
    @abstractmethod
    def do_step_1(self):
        # This method should be overriden
        pass

    @abstractmethod
    def do_step_2(self):
        # This method should be overriden
        pass

    def do_this_or(self):
        print('You can override me but you do not have to')

class ConcreteClassA(AbstractClass):
# This class inherits from the Abstract class featuring the template method   
    def do_step_1(self):
        print('Doing step 1 for ConcreteClassA ...')
    
    def do_step_2(self):
        print('Doing step 2 for ConcreteClassA ...')

class ConcreteClassB(AbstractClass):
# This class inherits from the Abstract class featuring the template method  
    def do_step_1(self):
        print('Doing step 1 for ConcreteClassB ...')
    
    def do_step_2(self):
        print('Doing step 2 for ConcreteClassB ...')
    
    def do_this_or(self):
        print('Doing my own business ...')

def main():
    print('--==ConcreteClassA==--')
    
    a = ConcreteClassA()
    a.template_method()

    print('--==ConcreteClassB==--')
    
    b = ConcreteClassB()
    b.template_method()

if __name__ == '__main__':
    main()
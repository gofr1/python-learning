#!/usr/bin/env python3

# All of this evaluates to False
#
# False and None
# Numeric zero values: 0, 0.0, 0j
# Decimal(0), Fraction(0,x)
# Empty sequences/collections: (), [], {}, ''
# Empty sets and ranges: set(), range(0)

# Anything else evaluates as True
# Except:

class myClass:
    def __bool__(self):
        return False
    
    def __len__(self):
        return 0

def main():
    """Examples of evaluating to False"""
    print(f'0 is {bool(0)}')
    print(f'Empty set is {bool(set())}')
    
    mc = myClass()
    print(f'myClass object is {bool(mc)}')

if __name__ == '__main__':
    main()
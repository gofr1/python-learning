#!/usr/bin/env python3

# when x = 5 and we change it to3 in kitten - it will be call-by value
# when we use list it is call-by-reference

def main():
    # x = 5
    x =[5]
    print('main', id(x)) # 648
    kitten(x)
    print('main', id(x)) # 648
    print('main', x)

def kitten(x):
    print('kitten', id(x)) # 648
    # x = 3 
    x[0] = 3
    print('kitten', id(x)) # 584
    print('Meow!')
    print('kitten', x)

def another():
    x = [5] # list is mutable
    y = x
    x[0] = 3
    print(id(x))
    print(id(y))
    print(id(x[0]))
    print(id(y[0]))
    print(x)
    print(y)

if __name__ == '__main__': 
    # another() 
    main()
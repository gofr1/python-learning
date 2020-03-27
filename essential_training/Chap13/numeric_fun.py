#!/usr/bin/env python3

def main():
    x = '42'
    y = int(x) # int is a constructor
    z = float(x)

    print(f'x is {type(x)}')
    print(f'x = {x}')
    print(f'y is {type(y)}')
    print(f'y = {y}')
    print(f'z is {type(z)}')
    print(f'z = {z}')

    # get absolute value
    x = -42
    y = abs(x)
    z = -42.3
    q = abs(z)

    print(f'x is {type(x)}')
    print(f'x = {x}')
    print(f'y is {type(y)}')
    print(f'y = {y}')
    print(f'z is {type(z)}')
    print(f'z = {z}')
    print(f'q is {type(q)}')
    print(f'q = {q}')
    
    # get the quotient and the remainder in a tuple
    x = 42
    print(divmod(x, 5))
    print((x//5, x%5))
    
    x = -42
    print(divmod(x, 5))
    print((x//5, x%5))    

if __name__ == '__main__':
    main()
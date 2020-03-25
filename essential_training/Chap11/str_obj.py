#!/usr/bin/env python3

# here we create new class MyString based on str built-in class
class MyString(str):
    def __str__(self):
        return self[::-1] # lets print backwards

def main():
    hello = 'Hello, World!'

    # common string methods
    print(hello.upper())
    print(hello.lower())
    print(hello.casefold()) # more strict than lower, will lower even unicode characters

    print(hello.capitalize())
    print(hello.title())
    print(hello.swapcase())
    
    # use of MyString class that print backwrads
    olleh = MyString(hello)
    print(olleh)
    
    # using format with variables
    hello += ' {}'
    print(hello.format(42))

    # string are immutable, so returned object is different object
    str1 = hello.upper()

    print('id of hello: {}, and hello = "{}"'.format(id(hello), hello))
    print('id of str1: {}, and str1 = "{}"'.format(id(str1),str1))

    # concatination
    s1 = 'Some string'
    s2 = 'and that is another one'
    print(s1 + ' ' + s2)

    s3 = 'one string' ' another one'
    print(s3)

    # formating
    x = 42 * 100000
    print('x = {:,.2f}'.format(x))
    y = 42
    print('Binary: {:b}'.format(y))
    print('Hexadecimal: {:x}'.format(y))
    print('Decimal: {:d}'.format(y))


if __name__ == '__main__':
    main()
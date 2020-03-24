#!/usr/bin/env python3

class RevStr(str):
    def __str__(self): # override a tring representation method
        return self[::-1]

def main():
    hello = RevStr('Hello, world.')
    print(hello)

if __name__ == '__main__':
    main()
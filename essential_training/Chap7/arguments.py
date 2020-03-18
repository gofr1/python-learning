#!/usr/bin/env python3

def main():
    x = kitten('meow', 'grrr', 'purr')
    print(type(x), x)

def kitten(*args): # variable length variable list (tuple)
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meow!')
    # if no return statement function will return None (NoneType)
    return dict(x = 42)
        

if __name__ == "__main__":
    main()
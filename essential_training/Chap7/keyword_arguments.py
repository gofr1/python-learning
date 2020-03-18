#!/usr/bin/env python3

def main():
    # kitten(kitty = 'meow', dog = 'grrr', cat = 'purr') 
    # # or
    x = dict(kitty = 'meow', dog = 'grrr', cat = 'purr') 
    kitten(**x)

def kitten(**kwargs): # keyword arguments list (dictionary)
    if len(kwargs):
        for k in kwargs:
            print('{} says: {}'.format(k, kwargs[k]))
    else:
        print('Meow!')

if __name__ == "__main__":
    main()
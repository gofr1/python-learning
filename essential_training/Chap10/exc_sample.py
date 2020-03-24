#!/usr/bin/env python3

from sys import exc_info

def main():
    try: #x = int('foo')
        x = 5/0
    except ValueError: print('I caught a ValueError')
    # except ZeroDivisionError: print('don\'t divide by zero!')
    except: print(f'Unknown error: {exc_info()}') # for any other error
    else: # will only be executed if I don't have an error
        print(f'good job! x = {x:2.4f}')

if __name__ == '__main__':
    main()
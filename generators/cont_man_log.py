#!/usr/bin/env python3

from contextlib import contextmanager
from datetime import datetime

HEADER = 'this is the header'
FOOTER = 'this is the footer'

@contextmanager # decorator
def new_log_file(name):
    try:
        logname = name
        f = open(logname, 'w')
        f.write(f'{get_datetime()} {HEADER} \n')
        yield f
    finally:
        f.write(f'{get_datetime()} {FOOTER} \n')
        print("Logfile created")
        f.close

def get_datetime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def main():
    with new_log_file('logfile.txt') as file:
        file.write(f'{get_datetime()} this is the body \n')

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# add execution permission for this file: chmod +x some_cmd.py 
# run it: ./some_cmd.py 1 2 3

import sys

def main():
    print(f"Number of arguments: {len(sys.argv)}")
    print(sys.argv)

    # remove some arguments
    sys.argv.remove(sys.argv[0])
    print(sys.argv)

    # doing something w/arguments
    summ = 0
    arguments = sys.argv
    for arg in arguments:
        try:
            number = int(arg)
            summ += number
        except Exception:
            print(f"Bad input, cannot convert \"{arg}\" into integer")
    print(f"Sum of arguments is: {summ}")

if __name__ == '__main__':
    main()
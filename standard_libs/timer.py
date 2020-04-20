#!/usr/bin/env python3

import time

def main():
    run = input("Start? > ")
    seconds = 0

    if run == 'y':
        while seconds != 10:
            print(f"> {seconds}")
            time.sleep(1)
            seconds += 1
        print(f"> {seconds}")

if __name__ == '__main__':
    main()
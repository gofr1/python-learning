#!/usr/bin/env python3

from datetime import datetime

def main():
    now = datetime.now()
    print(now.date())
    print(now.time())

    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)

if __name__ == '__main__':
    main()
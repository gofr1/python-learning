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

    # formatting date time
    print(now.strftime("%a %A %d")) # day
    print(now.strftime("%b %B %m")) # month
    print(now.strftime("%y %Y")) # year

    print(now.strftime("%H:%M:%S")) # time 24-H
    print(now.strftime("%I:%M:%S %p")) # time AM/PM

if __name__ == '__main__':
    main()
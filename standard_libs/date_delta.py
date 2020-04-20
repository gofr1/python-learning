#!/usr/bin/env python3

from datetime import datetime, timedelta
import calendar

def main():
    now = datetime.now()

    testDate = now + timedelta(days=2)
    fewWeeksAgo = now - timedelta(weeks=3)
    
    print(now.date())
    print(testDate.date())
    print(fewWeeksAgo.date())

    cal = calendar.month(2012, 1)
    print(cal)

    cal2 = calendar.weekday(2012, 1, 31)
    print(cal2)

    print(calendar.isleap(2020))
    
if __name__ == '__main__':
    main()
import calendar 

# text calendar
cal = calendar.TextCalendar(calendar.MONDAY)
print(cal.formatmonth(theyear = 2020, themonth = 3, w = 0, l = 0))

# html calendar
cal = calendar.HTMLCalendar(calendar.MONDAY)
print(cal.formatmonth(theyear = 2020, themonth = 3, withyear= True))

# loop over the days of month
cal = calendar.TextCalendar(calendar.MONDAY)
for i in cal.itermonthdays(2020, 3):
    print(i)

# provide name of months or weekdays etc.
for mnth in calendar.month_name:
    print(mnth)

for day in calendar.day_name:
    print(day)

# calculate days based on rule
# e.g. first friday of each month
for month in range(1,13):
    cal = calendar.monthcalendar(year = 2020, month = month)
    # first friday must be in a first two weeks of given month
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        needed_day = weekone[calendar.FRIDAY]
    else:
        needed_day = weektwo[calendar.FRIDAY]
    # and here we add nice output
    print("%10s %2d" % (calendar.month_name[month], needed_day))
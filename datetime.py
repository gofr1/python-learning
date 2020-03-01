from datetime import date, time, datetime, timedelta

# getting dates and time
today = date.today()

print("Today is", today)
print("Date components: day {}, month {}, year {}".format(today.day, today.month, today.year))
print("Today's weekday # is: ", today.weekday())

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Which is", days[today.weekday()])

cur_datetime = datetime.now()
print("Current date and time is", cur_datetime)
print("Current time is", cur_datetime.time())

# formatting dates and time
now = datetime.now()

print(now.strftime("Current year is %Y (or short %y)"))
print(now.strftime("%a, %d %B, %y"))

# https://strftime.org/ for more info
# locale’s appropriate date and time representation
print(now.strftime("Locale date and time: %c"))
print(now.strftime("Locale date: %x"))
print(now.strftime("Locale time: %X"))

print(now.strftime("Current time: %I:%M:%S %p"))
print(now.strftime("24H format: %H:%M:%S"))

# working with timedelta objects
print(timedelta(days=365, hours=5, minutes=1))
print("Today is:", cur_datetime ,"\nOne year from now:", str(cur_datetime + timedelta(days=365)))
print("One week later it was", str(cur_datetime + timedelta(weeks=-1)))

# how many days until some date
today = date.today()
some_date = date(now.year, 5, 9)

if some_date < today:
    print("Victory day was %d days ago" % ((today - some_date).days))
    some_date = some_date.replace(year= today.year + 1)
    print("It is just", (some_date - today).days , "till next Victory day")
elif some_date > today:
    print("Victory day will be in %d days" % ((some_date - today).days))
else:
    print("Victory day is today")

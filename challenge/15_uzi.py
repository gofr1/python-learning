import calendar

mon = 1 # January
day = 26
wd = 0 # Monday

for year in range(1046, 2006, 10):
    if (calendar.weekday(year = year, month = 1, day = 26) == 0):
        print(f'{year}-01-{day}')
#* 1046-01-26
#* 1176-01-26
#* 1226-01-26
#* 1356-01-26
#* 1446-01-26
#* 1576-01-26
#* 1626-01-26
#* 1756-01-26
#* 1846-01-26
#* 1976-01-26

# Comments from html page:
#* he ain't the youngest, he is the second
#* todo: buy flowers for tomorrow 

# So we need 27 of January and the second result from a query above (from the bottom)
# Let's check Wikipedia:
# 1846-01-27 - Nothing
# 1756-01-27 - Ta-dam! https://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart



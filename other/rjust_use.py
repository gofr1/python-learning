#!/usr/bin/env python3

title = 'Amount'
val1 = 600
val2 = 2500
val3 = 15

width = len(title)

# Return a right-justified string of length width.
print(f'{title}\n\
{str(val1).rjust(width)}\n\
{str(val2).rjust(width)}\n\
{str(val3).rjust(width)}')

#* Amount
#*    600
#*   2500
#*     15
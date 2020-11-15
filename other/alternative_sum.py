#!/usr/bin/env python3

# sum w/o: sum, import, while, for, reduce, map
def sum_ (lst):
    if len(lst) == 1:
        return lst[0]
    
    x = lst[0]
    y = sum_(lst[1:])

    return x + y 

ints = [4, 2, -43, 5, 6, 0]

print(sum_(ints))
print(sum(ints))
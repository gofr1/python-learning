#!/usr/bin/env python3

# Given a number x, determine whether the given number is Armstrong number or not. 
# A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.

# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 

def is_armstrong_num(number):
    res = 0
    num_str = str(number)
    if isinstance(number, int) and number > 0:
        l = len(num_str)
        for n in num_str:
            res += int(n) ** l
    if res == number:
        return True
    return False

print(is_armstrong_num(3))
#* True
print(is_armstrong_num(153))
#* True
print(is_armstrong_num(1569))
#* False
print(is_armstrong_num(1634))
#* True

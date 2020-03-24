#!/usr/bin/env python3

x = 0x0a
y = 0x02

print(f'(hex) x is {x:02x}, y is {y:02x}') # 0 - leading zero, 2 - number of chars, x - hexadecimal
print(f'(bin) x is {x:08b}, y is {y:08b}')

# & and 
print(f'(hex) & and {x & y:02x}') 
print(f'(bin) & and {x & y:08b}')

# | or
print(f'(hex) | or {x | y:02x}') 
print(f'(bin) | or {x | y:08b}')

# ^ xor
print(f'(hex) ^ xor {x ^ y:02x}') 
print(f'(bin) ^ xor {x ^ y:08b}')

# << shift left
print(f'(hex) << shift {x << y:02x}') 
print(f'(bin) << shift {x << y:08b}')

# >> shift right
print(f'(hex) >> shift {x >> y:02x}') 
print(f'(bin) >> shift {x >> y:08b}')
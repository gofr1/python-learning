charecter = 'a'
name = "Ilia"
with_quote = "I ain't gonna"
longer = """ This string
has multiple lines
in it
"""
escaped = 'I ain\'t gonna'
unicode_snake = 'I love \N{SNAKE}'
backslash = '\\'

strings = [charecter, name, with_quote, longer, escaped, unicode_snake, backslash]
print(strings)

# for regular expressions us r/re module

slash_t = r'\tText \\'
print(slash_t)
normal = '\tText \\'
print(normal)

# format

name = 'Ilia'
print('Hello {}'.format(name))

print('Int:{} Float:{} String:{}'.format(10, 2.5, 'foo'))

print('Name: {}'.format('Ilia'))
print('Name: {name}'.format(name = 'Ilia'))
print('Name: {[name]}'.format({'name':'Ilia'}))
print('last: {2} first: {0} middle: {1}'.format('Ilia','John','Neo'))

# :[[fill]allign][sign][#][0][width][grouping_option][.precision][type]

print("Name: {:*^12}".format("Ilia"))
print(-44/100)
print("Percent: {:=+10.2%}".format(-44/100))
print("Decimal: {:d}".format(12))
print("Binary: {:b}".format(12))
print("Hex: {:x}".format(12))

# f-string

print(f'Square root of 2 is {2**.5:2.4f}')
name = 'ilia'
print(f'Name: {name.capitalize()}')


# task1
print('{name} is {age}'.format(name = 'Ilia', age = '35'))

# task2
paragraph = '"Python is a great language!", said Fred. "I don\'t\never remember having this much fun before.'
print(paragraph)

# task3 

print('\N{GREEK CAPITAL LETTER OMEGA}')
print('\u03A9')

# task4 

item = 'car'
cost = 13499.99
print('{: <10}{: >10}'.format(item,cost))

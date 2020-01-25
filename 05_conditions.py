5 > 2

a = None
b = None
a is b
a is not b

name = 'Paul'
beatle = False
if name == 'George' or \
    name == 'Paul' or \
    name == 'John' or \
    name == 'Ringo':
    beatle = True
print(beatle)
# or
name = 'Paul'
beatle = False
if (name == 'George' or
    name == 'Paul' or
    name == 'John' or
    name == 'Ringo'):
    beatle = True
print(beatle)
#or
beatles = {'George', 'Paul', 'John' , 'Ringo'}
beatle = name in beatles
print(beatle)


score = 87
if score >= 90:
    grade = 'A'
elif score >= 80: # 'if' will find first 'elif' that evaluates True and use it
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade) # B

# task1

year = 2020
if year%4 == 0:
    year_type = 'leap'
else:
    year_type = 'normal'
print('This is %s year' % year_type)

# task2

some_number = 44
if some_number%2 == 0:
    some_number_type = 'even'
else:
    some_number_type = 'not even'
print('This number is %s' % some_number_type)

# task3

# my editor uses 4 spaces instead of tab
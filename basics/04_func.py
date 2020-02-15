dir('Ilia') # returns attributes (methods) of an object

# task1
name = 'Ilia'
dir(name)
help(name.find)
help(name.title)

# task2
age = 35
dir(age)
help(age.numerator)


# number methods

a=5
a.conjugate()

(5).conjugate()

# string methods

xl = 'some_file.xls'
xl.endswith('.xls')

word = 'grateful'
word.find('ate') # will return 2 (word is strting from 0)
word.find('great') # if not found -1

', '.join(['1','2','3'])

fname = 'readme.TXT'
fname.endswith('.txt') # false
fname.lower().endswith('.txt') # true

'Book'.startswith('b')
'Book'.startswith('B')

'   hello there!    '.strip()

'yell'.upper()

# task1

school = 'BIT'
dir(school)
help(school.rpartition)

# task2
country = 'Russia'
correct_country = country.upper()
correct_country

# task3
filename = 'hello.py'
filename.endswith('.java')
filename.find('.py')
filename.startswith('world')


# Boolean

bool('') # False

bool('0') # True
bool('1') # True
bool('01') # True
bool('False') # True

bool(0) # False
bool(1) # True

# int, float, bool, str are classes which are very similar to functions!

is_done = False
if is_done: # no need to use is_done == True or bool(is_done)
    'It is done!'
else:
    'Not done!'

members = []
if members:
    'There is some values!'
else:
    'There are no values!'

# None

bool(None) # False

# None is returned when function has no 'return'
# Operator 'is' is faster than '=='

a = None

if a is None:
    print('a is not set!')

if not a:
    print('a is not set!')

True is None


# task1

age = 35
old = None

if age > 18:
    old = True
else:
    old = False

print(old)

# task2
name = 'Ilia'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
second_half = None

if alphabet.find(name[0].lower()) < len(alphabet):
    second_half = False
else:
    second_half = True

print(second_half)

# task3

names = ['John', 'William', 'Antony']

if names:
    'Class has enrollments!'
else:
    'The class is empty!'

# task4

car = None
bool(car)

if car:
    'Taxi for you!'
else:
    'You have a car!'

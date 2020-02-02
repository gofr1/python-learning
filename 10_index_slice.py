my_pets = ["dog", "cat", "bird"]
my_pets[0] # first from left
my_pets[-1] # first from right (end)

# indexing could be used for tuples and strings:
('Fred', 23, 'Senior')[0] # Fred
'Fred'[0] # F

# a[-x] = a[len(a)-x]:
#
# 0 1 2 3 4 5 6 7
# d a t a . c s v
#-8-7-6-5-4-3-2-1
#

# slices
my_pets[0:2] #  ['dog', 'cat'] 
# 2 is last element but it is not included in slice

# [0:4] [-8:-4] [:4] - data
# [5:8] [5:] [-3:] - csv 
# from example above

dog_and_bird = my_pets[0:3:2]
print(dog_and_bird) # ['dog', 'bird']

zero_three_six = list(range(7))[::3]
print(zero_three_six)
# [0, 3, 6]

my_pets[::-1]
# ['bird', 'cat', 'dog'] 
# if minus value is specified - it goes backwards

[1, 2, 3, 4, 5][::-1]
#[5, 4, 3, 2, 1]

# with string it would be reversing
'ilia'[::-1]
# aili


# task1

my_name = "Ilia"
my_name[0:1] # or my_name[:1]
my_name[-1:]

# task2

def find_extension (file_name):
    return filename[filename.rfind('.')+1:]

filename = 'readme.txt'
find_extension(filename)

# task3
def is_palindrome (word):
    return True if word.lower() == word[::-1].lower() else False

is_palindrome('Ilia')
is_palindrome('abba')
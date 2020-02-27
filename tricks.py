# Trick #1
# Reversing a string in Python

a =  "uuuuffff"
print("Reverse is",a[::-1])
# Reverse is ffffuuuu

# Trick #2
# Transposing a Matrix
mat = [[1, 2, 3], [4, 5, 6]]
for m in zip(*mat):
    print(m)
# (1, 4)
# (2, 5)
# (3, 6)

# Trick #3
# Store all three values of the list in 3 new variables
a = [1,2,3]
a = [1, 2, 3]
x, y, z = a 
print("x = {}, y = {}, z = {}".format(x, y, z))
# x = 1, y = 2, z = 3

# Trick #4
# Create a single string from all the elements in list
a = ["I", "want", "to", "be", "a", "Python", "Developer"]
print(" ".join(a))
# I want to be a Python Developer

# Trick #5
list1 = ['a', 'b', 'c', 'd']
list2 = ['p', 'q', 'r', 's']
for x, y in zip(list1, list2):
   print(x, y)
# a p
# b q
# c r
# d s

# Trick #6
# Swap two numbers with one line of code.
a = 8
b = 7
b, a = a, b
print("a = {}, b = {}".format(a,b))
# a = 7, b = 8

# Trick #7
# Print some concatineted strings without using loops
print("some" * 4 + ' ' + 'mentor' * 5)
# somesomesomesome mentormentormentormentormentor

# Trick #8
# Convert list of lists to a single list without using any loops.
import itertools  
a = [[1, 2], [3, 4], [5, 6]]
list(itertools.chain.from_iterable(a))
# [1, 2, 3, 4, 5, 6]

# Trick #9
# Checking if two words are anagrams
from collections import Counter

def is_anagram(str1, str2):
     return Counter(str1) == Counter(str2)

is_anagram("abc","bcd") # False
is_anagram("abc","cba") # True

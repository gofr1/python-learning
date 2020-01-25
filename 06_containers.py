##############################
# lists (mutable)
##############################

names = list()
other_names = ['Fred', 'Charles']
# or
other_names = list(['Fred', 'Charles'])

list('Ilia')
# ['I', 'l', 'i', 'a']

names = list()
names.append('Ilia')
names.append('Alex')
names
names.clear()

# all methods are returning None by default (or if tell them to return smth else)

# indexes
names[0]
names[1]

# inserting

names.insert(0, 'George')
names

# changing

names[1] = 'Elijah'
names

# deleting

names.remove('Alex')
names

del names[1]
names

# sorting

names
names.sort()
names

old = [5, 3, -2, 1]
nums_sorted = sorted(old) # sorted creates new sorted list
# sorted is reusing elements of list, it dosn't create new ones
print(old)
print(nums_sorted)

things = [2, 'abc', 'Zebra', '1']
things.sort() # will give TypeError because elements are int and str (different types)

# you need to use 'key' parameter

things.sort(key=str)
print(things)

# useful

nums = range(5)
nums

list(nums) # [0, 1, 2, 3, 4] not 5! all is starting with zero

nums2 = range(2, 6)
list(nums2) # [2, 3, 4, 5]

even = range(0, 11, 2)
list(even) # [0, 2, 4, 6, 8, 10]

smth = range(0, -11, -2)
list(smth)  #[0, -2, -4, -6, -8, -10]

a = range(0, 5)
b = range(5, 10)
both = list(a) + list(b)
len(both)
print(both)

##############################
# Tuples
##############################
# they are immutable
# can store duplicates
# are indexed

row = ('George', 'Guitar')
print(row)
id(row)

row2 = ('Paul', 'Bass')
print(row2)
id(row2)

# create

# empty tuple
empty = tuple()
print(empty)

empty = ()
print(empty)

# with 1 element
# if you use one = (1) it would be integer variable 
one = tuple([1])
print(one)

one = (1,)
print(one)

one = 1,
print(one)

# with more than 1 element

p = tuple(['Sid', 'Paul', 'Jim'])
print(p)

p = 'Sid', 'Paul', 'Jim'
print(p)

p = ('Sid', 'Paul', 'Jim')
print(p)

# you cannot append, insert or delete from tuple

##############################
# Sets
##############################
# they are immutable
# cannot store duplicates
# are indexed
# use hashes

# create

digits = [0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
digits_set = set(digits)
print(digits_set) # duplicate values are gone

digits_set = {0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(digits_set) 

print(9 in digits_set) # use 'is' to check if element is in set
print(42 in digits_set)

# logical operations
digits_set = {0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9}
odd = {1, 3, 5, 7, 9}

even = digits_set - odd
print(even) # {0, 2, 4, 6, 8}

prime = {2, 3, 5, 7}
prime_even = prime & even
print(prime_even) #  {2} - because this element is in both sets

numbers = odd | even
print(numbers) # sorted ???

first_five = set([0, 1, 2, 3, 4, 5])
two_to_six = set([2, 3, 4, 5, 6])
in_one = first_five ^ two_to_six
print(in_one) #  {0, 1, 6}

# 'in' for sets is working faster than for lists


# task1
# list
colleagues = ['Pavel', 'Sergey', 'Artur', 'Oksana']
id(colleagues)
print(colleagues)
colleagues.sort()
print(colleagues)
id(colleagues)

print(colleagues[0])
print(colleagues[1])

# task2
# tuple
my_data = ('ilia', 'odintsov', '1984-12-17', 35)
people = []
people.append(my_data)
print(people)

pavel_data = ('pavel', 'botygin', '1980-05-01', 39)
oksana_data = ('oksana', 'matchenko', '1990-06-30', 29)
people.append(pavel_data)
people.append(oksana_data)
print(people)

people.sort()
print(people)

# task3

names = set(['Maria', 'Pavel', 'Sergey', 'Artur', 'Oksana', 'Alexander'])
popular_names = set(['Julia', 'Jack', 'Andrew', 'Sofia', 'Petr', 'Maria', 'Ivan', 'Alexander', 'Anna', 'Muhammed'])
print(names & popular_names)

# task4

shakespeare = """   Cap. Doubtfull it stood,
As two spent Swimmers, that doe cling together,
And choake their Art: The mercilesse Macdonwald
(Worthie to be a Rebell, for to that
The multiplying Villanies of Nature
Doe swarme vpon him) from the Westerne Isles
Of Kernes and Gallowgrosses is supply'd,
And Fortune on his damned Quarry smiling,
Shew'd like a Rebells Whore: but all's too weake:
For braue Macbeth (well hee deserues that Name)
Disdayning Fortune, with his brandisht Steele,
Which smoak'd with bloody execution
(Like Valours Minion) caru'd out his passage,
Till hee fac'd the Slaue:
Which neu'r shooke hands, nor bad farwell to him,
Till he vnseam'd him from the Naue toth' Chops,
And fix'd his Head vpon our Battlements """

waldo = """When we speak of nature in this manner, we have a distinct 
but most poetical sense in the mind. We mean the integrity of 
impression made by manifold natural objects. It is this which 
distinguishes the stick of timber of the wood-cutter, from the tree 
of the poet. The charming landscape which I saw this morning, is 
indubitably made up of some twenty or thirty farms. Miller owns this 
field, Locke that, and Manning the woodland beyond. But none of them 
owns the landscape. There is a property in the horizon which no man has
 but he whose eye can integrate all the parts, that is, the poet. This 
 is the best part of these men's farms, yet to this their 
 warranty-deeds give no title."""

shakespeare_words = set(shakespeare.split(' '))
waldo_words = set(waldo.split(' '))

both = shakespeare_words & waldo_words
not_both = shakespeare_words - waldo_words

print(both)
print(not_both)

# task5
tuple_properties = set(dir(tuple))
list_properties = set(dir(list))

type(tuple_properties)
type(list_properties)

print(tuple_properties)
print(list_properties)

print(list_properties - tuple_properties)
print(tuple_properties - list_properties)
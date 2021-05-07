# using a hashtable to count indivisual items

# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
        "orange", "apple", "pear", "banana", "orange", 
        "apple", "kiwi", "pear", "apple", "orange"]

# create a hashtable object to hold the items and counts
counter = dict()

# iterate over each item and increment the count for each one
for item in items:
    if (item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

# print the results
print(counter)

# for item in items:
#     counter.setdefault(item, 0)
#     counter[item] += 1

# print(counter)

# One-Liner to count elements in the list
counter = {item: items.count(item) for item in set(items)}
print(counter)
# use a hashtable to filter out duplicate values

# define a set of items that we want to reduce the duplicates
items = ["apple", "pear", "orange", "banana", "apple",
        "orange", "apple", "pear", "banana", "orange", 
        "apple", "kiwi", "pear", "apple", "orange"]

# create a hashtable to perform a filter
filter = dict()

# loop over each itemand add to the hashtable
for key in items:
    filter[key] = 0

# create a set fromthe resulting keysin the hashtable
result = set(filter.keys())
print(result)

# print(set(items))
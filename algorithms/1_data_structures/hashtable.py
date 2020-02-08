# demo of hashtable usage

# create hashtable all at once
items1 = dict({"key1": 1, "key2": 2, "key3": "three"})
print(items1)

# create hashtable progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)

# try to accee=ss notexistent key
# print(items1["key6"])

# replace an item
items2["key2"] = 'two'
print(items2)

# iterate the keys and values in a dictionary
for key, value in items2.items():
    print("Key: ", key, " Value: ", value)
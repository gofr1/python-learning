
#    List is a collection which is ordered and changeable. Allows duplicate members.
#    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#    Set is a collection which is unordered and unindexed. No duplicate members.
#    Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Arrays
cars = ["Ford", "Volvo", "BMW"] 
print(cars)


for i in range(0, len(cars)):
    print(cars[i])

for i in cars:
    print(i)

cars.append("Skoda")

print(cars)

# Lists
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1] = "blackcurrant"
print(thislist)

for x in thislist:
    print(x) 
# Tuples

thistuple = ("apple", "banana", "cherry")
#'tuple' object does not support item assignment
#thistuple[1] = "blackcurrant"
# The values will remain the same:
print(thistuple)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x) 

#sets

thisset = {"apple", "banana", "cherry"}
print(thisset) 

# Dictionaries
thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

thisdict =	{ 0: {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
},
1: {
    "brand": "Lamborgini",
    "model": "Diablo",
    "year": 1990
}
}
print(thisdict[0]["brand"])
print(len(thisdict))
thisdict.update( {2: {
    "brand": "Ferrari",
    "model": "F40",
    "year": 1984}
})
print(thisdict[2]["brand"])
print(len(thisdict))
print(thisdict)





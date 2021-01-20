#!/usr/bin/env python3

# Creates a new type object
NewType = type("NewType", (object, ), {"attr": "it is a new type"})
New = NewType()
  
# Print the type of object 
print(type(New))
#* <class '__main__.NewType'>
  
# Print the attribute of object 
print(New.attr)
#* it is a new type

# it is same as:
class NewType:
    attr = "it is a new type"

# Initialize an object 
New = NewType()
  
# Print the type of object 
print(type(New))

# Print the attribute of object 
print(New.attr)

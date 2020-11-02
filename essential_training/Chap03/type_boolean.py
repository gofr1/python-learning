#!/usr/bin/env python3
# "", 0, None evaluate as False

some_data = ("", 0, None, 'x', 1, True, False)

for data in some_data:
    evaluates = True if data else False # here is ternary conditional operator
    print("value '{}' evaluates as {}".format(data, evaluates))

# value '' evaluates as False
# value '0' evaluates as False
# value 'None' evaluates as False
# value 'x' evaluates as True
# value '1' evaluates as True
# value 'True' evaluates as True
# value 'False' evaluates as False

# more obscure and not widely used example involves tuples
isPlayful = True
dogPersonality = ('grim', 'playful')[isPlayful]
print(f'The dog is {dogPersonality}')
#* The dog is playful

# ShortHand ternary
True or 'Some'
#* True
False or 'Some'
#* 'Some'

# Some example
def masking(realName, someAlias = None):
    someAlias = someAlias or realName
    return someAlias

masking('John Doe')
#* 'John Doe'
masking('John Doe', 'nom de guerre')
#* 'nom de guerre'
import re

# Matching Regex Objects
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 555-123-4567.')
print('Phone number found: ' + mo.group())

# Adding parentheses will create groups in the regex
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 555-123-4567.')
print('Phone number found: ' + mo.group())

# Let's take a look what is in the groups
mo.group(1)
#* '555'
mo.group(2)
#* '123-4567'
mo.group(0)
#* '555-123-4567'
mo.group()
#* 555-123-4567
mo.groups()
#* ('555', '123-4567')

# It's useful to somehow separate the values
areaCode, mainNumber = mo.groups()
print(areaCode)
#* 555
print(mainNumber)
#* 123-4567
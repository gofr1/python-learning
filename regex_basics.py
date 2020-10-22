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

# Matching Multiple Groups with the Pipe
someRegex = re.compile (r'John Smith|Jane Doe')
mo1 = someRegex.search('John Smith and Jane Doe')
mo1.group()
#* 'John Smith'
mo2 = someRegex.search('Jane Doe and John Smith')
mo2.group()
#* 'Jane Doe'

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
#* 'Batmobile'
mo.group(1)
#* 'mobile'

# Optional Matching with the Question Mark
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
#* 'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
#* 'Batwoman'

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 777-123-4567')
mo1.group()
#* '777-123-4567'

mo2 = phoneRegex.search('My number is 123-4567')
mo2.group()
#* '123-4567'

# Matching Zero or More with the Star
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
#* 'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
#* 'Batwoman'

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
#* 'Batwowowowoman'

# Matching One or More with the Plus
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()
#* 'Batwoman'

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()
#* 'Batwowowowoman'

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None
#* True

# Matching Specific Repetitions with Braces
naRegex = re.compile(r'(Na){3}')
mo1 = naRegex.search('NaNaNa')
mo1.group()
#* 'NaNaNa'

mo2 = naRegex.search('Na')
mo2 == None
#* True


# 6
import requests
from zipfile import ZipFile, ZipInfo

url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
file_path = '/tmp/channel.zip'
help_file = 'readme.txt'

# write bytes of url content to variable
bin_content = requests.get(url).content

# write bytes in fyle
with open(file_path, 'wb') as fout:
    fout.write(bin_content)

# print content of readme file from archive
with ZipFile(file_path, 'r') as zout:
    if help_file in zout.namelist():
        print(zout.read(help_file).decode('utf8'))

# file mentioned in readme
# will start from this file
file_ext = '.txt'
start_from = '90052'
current_file = start_from + file_ext
comments = ''

# iterate through files and get comments from files
# in same direction @of nothing@ described in files
with ZipFile(file_path, 'r') as zout:
    while current_file in zout.namelist():
        file_content = zout.read(current_file).decode('utf8')
        comments += zout.getinfo(current_file).comment.decode('utf8')
        try:
            current_file = file_content.split(' ')[3] + file_ext
        except IndexError:
            print(file_content)
            break
        else:
            continue

print(comments) 

result = ''
for symbol in comments:
    if (symbol not in result and symbol.lower() != symbol.upper()):
        result += symbol
print(result.lower())
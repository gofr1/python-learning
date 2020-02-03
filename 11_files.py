# open(filename, mode='r', buffering=-1, encoding=None,
# errors=None, newline=None, closefd=True, opener=None)
# for windows use r"path_to_file" (r means raw string)
# so c:\test will not consider \t as tab

# modes
# r - read (default)
# w - write (overwrite if file exist)
# x - write (FileExistsError if file is already there)
# a - write to the end of file
# rb - read of binary file
# wb - write binary file (overwrite if exists)
# w+b - opens binary file for read and write
# xb - write to binary file (FileExistsError if file is already there)
# ab - write to the end of binary file

a_file = open('/tmp/a.txt', 'w')

passwd_file = open('/etc/passwd') # returns an instance of file object
#passwd_file.readline() # returns one line
#passwd_file.readlines() # returns all lines in one line
print(passwd_file.read()) # returns all file content
passwd_file.close() # don't forget to close!

# fin - file input
# fout - file output
# fp - file pointer

# Read Binary
bfin = open('/home/user/Documents/img.png', 'rb')
bfin.read(8)
bfin.close()

# iterate through rows of file
fin = open('/etc/passwd') 
for line in fin.readlines():
    print(line)
fin.close()
# but it is better use another way, because readlines loads
# all content...
fin = open('/etc/passwd') 
for line in fin: # and here it takes it one by one
    print(line)
fin.close()
# method __iter__ for file class is used

# Write to file
fout = open('/tmp/names.txt', 'w')
fout.write('Ilia\n')
fout.close()

# \n is used in unix-like systems for new string
# \r\n is for Windows
# better use os.linesep to get right new string symbol

import os
os.linesep

# to force-write in file you can use flush
# anyway it will be saved on close

# why you should close the file?
# - if file is stored in global variable it will never be closed during execution
# - w/o flush you will never when data will be written to file
# - there maybe OS specific settings for number of simultaneously opened files
# - some OS deny deleting opened files
# you can use with:

with open('/tmp/names.txt', 'w') as fout3:
    fout3.write('Boom!\n')
# it is the same as
fout3 = open('/tmp/names.txt', 'w')
fout3.write('Ilia\n')
fout3.close()

def add_numbers(filename):
    results = []
    with open(filename) as fin:
        for num, line in enumerate(fin):
            results.append('{0} - {1}'.format(num, line))
        return results

add_numbers('/tmp/names.txt')

# another way:

def add_numbers(filename):
    with open(filename) as fin:
        return add_nums_to_seq(fin)

def add_nums_to_seq(seq): # can be used with any data sequence
    results = []
    for num, line in enumerate(seq):
        results.append('{0} - {1}'.format(num, line))
    return results

add_numbers('/tmp/names.txt')

# task1

def write_csv(filename, some_data):
    fout = open(filename,'w')
    i = 1
    for seq in some_data:
        row = ''
        header = ''
        for key, value in seq.items():
            header += key +','
            row += value + ','
        fout.write(header[:-1]+'\n') if i == 1 else None
        i += 1   
        fout.write(row[:-1]+'\n')
    fout.close()

books = [{
         "id": "01",
         "language": "Java",
         "edition": "third",
         "author": "Herbert Schildt"
      },
      {
         "id": "07",
         "language": "C++",
         "edition": "second",
         "author": "E.Balagurusamy"
      }]
filename = '/tmp/books.csv'

write_csv(filename, books)

# task2
def read_csv(filename):
    fin = open(filename)
    rows = []
    for row in fin:
        rows.append(row.split(','))
    fin.close()
    
    container = {}
    results = []
    for i in range(1,len(rows)):
        for k in range(len(rows[i])):
            container.setdefault(rows[0][k], rows[i][k])
        results.append(container)
    return results

read_csv(filename)
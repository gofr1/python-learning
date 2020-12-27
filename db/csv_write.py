#!/usr/bin/env python3

import csv

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])

outputFile.close()

# output.csv:
#* spam,eggs,bacon,ham
#* "Hello, world!",eggs,bacon,ham
#* 1,2,3.141592,4
#* 

# will recreate file an
with open('output.csv', 'w', newline='') as outputFile: 
    outputWriter = csv.writer(outputFile) #some options: delimiter='\t', lineterminator='\n\n'

    outputWriter.writerow(['apple', 'tomato', 'orange', 'watermelon'])
    outputWriter.writerow(['Hello, world!', 'That\'s', 'me', '!'])
    outputWriter.writerow([0, 1, 1, 2])

# output.csv:
#* apple,tomato,orange,watermelon
#* "Hello, world!",That's,me,!
#* 0,1,1,2
#* 

with open('outputWithHeader.csv', 'w', newline='') as outputFile:
    outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
    outputDictWriter.writeheader()

    outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
    outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
    outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})

# outputWithHeader.csv
#* Name,Pet,Phone
#* Alice,cat,555-1234
#* Bob,,555-9999
#* Carol,dog,555-5555
#* 
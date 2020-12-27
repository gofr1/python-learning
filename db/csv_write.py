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
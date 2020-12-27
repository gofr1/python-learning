#!/usr/bin/env python3

import csv

sampleFile = open('sample.csv')
sampleReader = csv.reader(sampleFile)
sampleData = list(sampleReader)
sampleData # the CSV file as a list of lists
#* [['4/5/2015 13:34', 'Apples', '73'], ... ['4/10/2015 2:40', 'Strawberries', '98']]

print(sampleData[0][0])

# reading in a loop
with open('sample.csv', newline='') as csvfile: # read by default
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print('; '.join(row))
#* 4/5/2015 13:34; Apples; 73
#* ...
#* 4/10/2015 2:40; Strawberries; 98
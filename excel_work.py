#!/usr/bin/env python3
# pip install openpyxl

import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string

# open file
wb = openpyxl.load_workbook('example.xlsx')
type(wb)
#* <class 'openpyxl.workbook.workbook.Workbook'>

# get sheet's names
wb.get_sheet_names()
#* ['Sheet1', 'Sheet2', 'Sheet3']

# select one sheet to work with
sheet = wb['Sheet1']
sheet
#* <Worksheet "Sheet1">
type(sheet)
#* <class 'openpyxl.worksheet.worksheet.Worksheet'>
sheet.title
#* 'Sheet1'

# get the workbook’s active sheet
anotherSheet = wb.active
anotherSheet
#* <Worksheet "Sheet1">

# working with cells
sheet['A1']
#* <Cell 'Sheet1'.A1>
sheet['A1'].value
#* '4/5/2015 1:34:02 PM'

c = sheet['B1']
c.value
#* 'Apples'

print(f'Row {c.row}, Column {c.column} is {c.value}')
#* Row 1, Column 2 is Apples
print(f'Cell {c.coordinate} is {c.value}')
#* Cell B1 is Apples
sheet['C1'].value
#* 73


sheet.cell(row=1, column=2)
#* <Cell 'Sheet1'.B1>
sheet.cell(row=1, column=2).value
#* 'Apples'

for i in range(1, 8, 2):
    print(i, sheet.cell(row=i, column=2).value)
#* 1 Apples
#* 3 Pears
#* 5 Apples
#* 7 Strawberries

sheet.max_row
#* 7
sheet.max_column
#* 3

get_column_letter(1)
#* 'A'
get_column_letter(900)
#* 'AHP'
get_column_letter(sheet.max_column)
#* 'C'
column_index_from_string('AA')
#* 27

# Getting Rows and Columns from the Sheets
tuple(sheet['A1':'C3'])
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(f'{cellObj.coordinate} - {cellObj.value}')

#* A1 - 4/5/2015 1:34:02 PM
#* B1 - Apples
#* C1 - 73
#* A2 - 4/5/2015 3:41:23 AM
#* B2 - Cherries
#* C2 - 85
#* A3 - 4/6/2015 12:46:51 PM
#* B3 - Pears
#* C3 - 14

# create and save Excel document
wb = openpyxl.Workbook()
wb.get_sheet_names()
#* ['Sheet']

sheet = wb.active
sheet.title
#* 'Sheet'

sheet.title = 'New sheet name'
wb.get_sheet_names()
#* ['New sheet name']

wb.save('example_copy.xlsx')

# create and remove of sheets
wb.create_sheet(index=0, title='First Sheet')
#* <Worksheet "First Sheet">
wb.create_sheet(title='Last Sheet')
#* <Worksheet "Last Sheet">

wb.get_sheet_names()
#* ['First Sheet', 'New sheet name', 'Last Sheet']

wb.remove(wb.get_sheet_by_name('Last Sheet'))

wb.get_sheet_names()
#* ['First Sheet', 'New sheet name']

# writing to cell
sheet = wb.get_sheet_by_name('First Sheet')
sheet['A1'] = 'Hello world!'
sheet['A1'].value
#* 'Hello world!'

wb.save('example_copy.xlsx')
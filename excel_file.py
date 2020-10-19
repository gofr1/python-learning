#!/usr/bin/env python3
import openpyxl

def create_file(flnm):
    wb = openpyxl.Workbook()
    sheet = wb.active
    
    sheet['A1'] = 'Row'
    sheet['B1'] = 'Text'
    sheet['C1'] = 'Value'
    sheet['D1'] = 'Comment'
    sheet['E1'] = 'Col2'
    sheet['F1'] = 'Col3'
    sheet['G1'] = 'Col4'
    sheet['H1'] = 'Col5'
    
    for i in range(2, 12): 
        sheet['A' + str(i)] = i
        sheet['B' + str(i)] = f'Test {i}'
        sheet['C' + str(i)] = (i * 10)
        sheet['D' + str(i)] = f'Row {i} - Test {i} = {(i * 10)}' 
    
    sheet.column_dimensions['B'].width = 20
    sheet.column_dimensions['D'].width = 30

    sheet.freeze_panes = 'A2'

    sheet['C12'] = '=SUM(C2:C11)'
    
    wb.save(flnm)
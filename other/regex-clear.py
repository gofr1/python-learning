import re
from prettytable import PrettyTable

values = ('(1,256,436.00) CAD',
'(1,344)',
'(112)',
'112',
'18,678.56',
'$ (56,890.04)',
'$ 56,678',
'(2)',
'(1,344) IND',
'(9,072.00)',
'(8,373) CAD',
'3,900 CAD')

digits = re.compile(r'([0-9.(])')

table = PrettyTable()
table.field_names = ['Old', 'New']

for val in values:
    table.add_row( [
        val,
        float(''.join(digits.findall(val)).replace('(','-'))
    ])

table.align = 'r'

print(table)
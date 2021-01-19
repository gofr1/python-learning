#!/usr/bin/env python3

# sudo pip3 install prettytable
# PrettyTable is for output table in a pretty format.

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['Name', 'Age', 'City']

table.add_row(["Alice", 34, "New York"])
table.add_row(["Bob", 23, "Saint-Petersburg"])
table.add_row(["Chris", 21, "Paris"])
table.add_row(["Tom", 27, "Sydney"])
table.add_row(["Betty", 32, "Melbourne"])

print(table)

#* +-------+-----+------------------+
#* |  Name | Age |       City       |
#* +-------+-----+------------------+
#* | Alice |  34 |     New York     |
#* |  Bob  |  23 | Saint-Petersburg |
#* | Chris |  21 |      Paris       |
#* |  Tom  |  27 |      Sydney      |
#* | Betty |  32 |    Melbourne     |
#* +-------+-----+------------------+

# change text align
table.align = 'r'
print(table)
#* +-------+-----+------------------+
#* |  Name | Age |             City |
#* +-------+-----+------------------+
#* | Alice |  34 |         New York |
#* |   Bob |  23 | Saint-Petersburg |
#* | Chris |  21 |            Paris |
#* |   Tom |  27 |           Sydney |
#* | Betty |  32 |        Melbourne |
#* +-------+-----+------------------+

# sorting
table.sortby = "City"
print(table)
#* +-------+-----+------------------+
#* |  Name | Age |             City |
#* +-------+-----+------------------+
#* | Betty |  32 |        Melbourne |
#* | Alice |  34 |         New York |
#* | Chris |  21 |            Paris |
#* |   Bob |  23 | Saint-Petersburg |
#* |   Tom |  27 |           Sydney |
#* +-------+-----+------------------+
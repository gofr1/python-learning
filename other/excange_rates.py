#!/usr/bin/env python3

import requests, json
from datetime import datetime
from prettytable import PrettyTable

ratio_date = datetime.now().date().isoformat() # for current ratio use latest
url = f'https://api.exchangeratesapi.io/{ratio_date}?base='

currencies = ['EUR', 'USD']

table = PrettyTable()
table.field_names = ['Date', 'Currency', 'RUB', 'CZK']

for currency in currencies:
    responce = requests.get(f'{url}{currency}')
    content = responce.content
    rate = json.loads(content)
    table.add_row([
        rate['date'],
        currency,
        "%.2f" % rate['rates']['RUB'],
        "%.2f" % rate['rates']['CZK']
    ])

table.align = 'l'
print(table)

#* +------------+----------+-------+-------+
#* | Date       | Currency | RUB   | CZK   |
#* +------------+----------+-------+-------+
#* | 2021-03-18 | EUR      | 88.13 | 26.17 |
#* | 2021-03-18 | USD      | 73.99 | 21.97 |
#* +------------+----------+-------+-------+
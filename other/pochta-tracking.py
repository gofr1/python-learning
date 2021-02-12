import requests, json
from prettytable import PrettyTable

url = 'https://www.pochta.ru/tracking'
barcode = 'Enter tracking barcode'

parameters = {
    'p_p_id': 'trackingPortlet_WAR_portalportlet',
    'p_p_lifecycle': 2,
    'p_p_state': 'normal',
    'p_p_mode': 'view',
    'p_p_resource_id': 'tracking.get-by-barcodes',
    'p_p_cacheability': 'cacheLevelPage',
    'p_p_col_id': 'column-1',
    'p_p_col_count': 1,
    'barcodes': barcode
}

responce = requests.get(url, params = parameters)

content = responce.content
info = json.loads(content)
table = PrettyTable()
details = PrettyTable()

table.field_names = ['PostId', 'Title', 'Weight', 'Sender', 'Recipient']
details.field_names = ['Date', 'Status', 'ZIP code', 'Country', 'City', ]

table.add_row( [
    info['response'][0]['formF22Params']['PostId'],
    info['response'][0]['trackingItem']['title'],
    info['response'][0]['trackingItem']['weight'],
    info['response'][0]['trackingItem']['sender'],
    info['response'][0]['trackingItem']['recipient']
])

history_length = len(info['response'][0]['trackingItem']['trackingHistoryItemList'])

for i in range(history_length-1):
    details.add_row( [
        info['response'][0]['trackingItem']['trackingHistoryItemList'][i]['date'],
        info['response'][0]['trackingItem']['trackingHistoryItemList'][i]['humanStatus'],
        info['response'][0]['trackingItem']['trackingHistoryItemList'][i]['index'],
        info['response'][0]['trackingItem']['trackingHistoryItemList'][i]['cityName'],
        info['response'][0]['trackingItem']['trackingHistoryItemList'][i]['countryName']
    ])

print(table)
print(details)
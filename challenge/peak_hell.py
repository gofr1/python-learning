# 5
import requests, pickle

pickle_file = '/tmp/banner.p'
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
content = requests.get(url).text[:]

# write data from url to file
with open(pickle_file, 'w') as fio:
    fio.writelines(content)

# read data from pickle file
with open(pickle_file, 'rb') as fout:
    ret_data = pickle.Unpickler(fout).load()

results = ''
for row_data in ret_data:
    for column_data in row_data:
        results += column_data[0] * column_data[1]
    results += '\n'
print(results)
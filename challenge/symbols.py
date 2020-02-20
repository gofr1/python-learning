# 2
import requests

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

page_contents = requests.get(url).text[:]
contents = page_contents.split('<!--')
parse_contents = dict()

for symbol in contents[-1]:
    m = parse_contents.setdefault(symbol,0)
    parse_contents[symbol] +=1

message = ''
for key, value in parse_contents.items():
    message += key if value == 1 else ''

print(message)


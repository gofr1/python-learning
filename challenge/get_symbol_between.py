# 3
import requests

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

page_contents = requests.get(url).text[:]
contents = page_contents.split('<!--')
parse_contents = dict()
len_str = 7
content_to_parse = contents[-1].split('\n')

message = ''

for string in content_to_parse:
    i = 0
    while i < len(string) - len_str:
        str_check = string[i:i+len_str]
        if str_check[:3] == str_check[:3].upper() and str_check[4:] == str_check[4:].upper() and str_check[3:4] == str_check[3:4].lower():
            message += str_check[3:4]
        i += 1
    message += '\n'

print(message)


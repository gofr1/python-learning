# 3
import requests

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

page_contents = requests.get(url).text[:]
contents = page_contents.split('<!--')
parse_contents = dict()
len_str = 7
content_to_parse = contents[-1].split('\n')

message = dict()

for string in content_to_parse:
    i = 0
    while i < len(string) - len_str:
        str_check = string[i:i+len_str]
        if str_check[:3] == str_check[:3].upper() and str_check[4:] == str_check[4:].upper() and str_check[3] == str_check[3].lower():
            m = message.setdefault(str_check[3],0)
            message[str_check[3]] +=1
        i += len_str
    # message += '\n'

{k: v for k, v in sorted(message.items(), key=lambda item: item[1], reverse=True)}


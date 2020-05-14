# 8
from ast import literal_eval
import requests
import bz2

standard_url = "http://www.pythonchallenge.com/pc/def/"

url = f"{standard_url}integrity.html"

page_contents = requests.get(url).text[:]
contents = page_contents.split('<!--')

data = contents[1].split('\n')
auth_dic = dict([(data[1][:2], data[1][5:-1]), (data[2][:2], data[2][5:-1])])

with open('un.bz2', 'wb') as f:
    f.write(literal_eval("b'{}'".format(auth_dic['un'])))

with open('pw.bz2', 'wb') as f:
    f.write(literal_eval("b'{}'".format(auth_dic['pw'])))

with bz2.BZ2File('un.bz2', 'r') as fr:
    un = fr.read()

with bz2.BZ2File('pw.bz2', 'r') as fr:
    pw = fr.read()

print(f"un: '{un.decode('utf8')}'\npw: '{pw.decode('utf8')}'")
#17
import requests
import bz2
from urllib.parse import unquote_to_bytes

session = requests.Session()

# from 4th task
first_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
response = session.get(first_url)

# standard_url = "http://www.pythonchallenge.com/pc/return/"
# url = f"{standard_url}romance.html"
# response = session.get(url, auth = HTTPBasicAuth('huge', 'file'))

print(response.cookies.get_dict())
#* {'info': 'you+should+have+followed+busynothing...'}

# Back to number 17, but instead of ?nothing use ?busynothing
new_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php/?busynothing'
response = session.get(new_url)

all_busynothings = dict()
all_busynothings[0] = '12345' #response.text.split('is ')[1]
start_from = 1
a = 0
cookie = ''

# number of tries
num_tries = 200

# and all the next 
for i in range(start_from, num_tries):
    next_url = new_url + '=' + str(int(all_busynothings[i-1]))
    response = session.get(next_url)
    print(f'Try {i}: {response.text}. Cookie: {response.cookies.get_dict()}')
    cookie += response.cookies.get_dict()['info']
    all_busynothings[i] = response.text.split('is ')[1]

print(cookie)

res = unquote_to_bytes(cookie.replace("+", " "))
print(res)

print(bz2.decompress(res).decode())
#* is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
# Farther of Mozart name is Leopold
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET 

standard_url = "http://www.pythonchallenge.com/pc/return/"
url = f"{standard_url}disproportional.html"
response = requests.get(url, auth = HTTPBasicAuth('huge', 'file'))
page_contents = BeautifulSoup(response.text, 'html.parser')
contents = page_contents.find_all('area')[0].get('href')

phonebook = standard_url.replace('return/',contents.split('/')[1])

deal = requests.get(phonebook)
print(deal.text)

# POST /xmlrpc HTTP 1.0
headers = {'Content-Type': 'text/xml;charset=utf-8', 'User-Agent': 'myXMLRPCClient/1.0'}

post_values = """<?xml version="1.0"?>
<methodCall>
   <methodName>phone</methodName>
      <params>
         <param>
            <value><string>Leopold</string></value>
         </param>
      </params>
</methodCall>
"""

x = requests.post(phonebook, data = post_values, headers = headers)
print(x.text)

xml_response = ET.fromstring(x.text.replace('\n',''))
phone = xml_response[0][0][0][0].text

print(phone)
#* 555-VIOLIN

# http://www.pythonchallenge.com/pc/return/violin.html
#* no! i mean yes! but ../stuff/violin.php. 

url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
response = requests.get(url, auth = HTTPBasicAuth('huge', 'file'), headers=  { "Cookie": "info=the flowers are on their way" })
print(response.text)
#* oh well, don't you dare to forget the balloons.
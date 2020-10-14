#13
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
            <value><string>Bert</string></value>
         </param>
      </params>
</methodCall>
"""

# He is not the evil - with any string
# let's take Bert from previous task

x = requests.post(phonebook, data = post_values, headers = headers)
print(x.text)

xml_response = ET.fromstring(x.text.replace('\n',''))
phone = xml_response[0][0][0][0].text

print(phone)
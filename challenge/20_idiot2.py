#20
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth

standard_url = "http://www.pythonchallenge.com/pc/hex/"
url = f"{standard_url}idiot2.html"
response = requests.get(url, auth = HTTPBasicAuth('butter', 'fly'))
page_contents = BeautifulSoup(response.text, 'html.parser')

print(page_contents)

#* <img border="0" src="unreal.jpg"/>
#* but inspecting it carefully is allowed.

# get the image
pic_name = page_contents.find_all('img')[0].get('src')

# and get it
response = requests.get(f'{standard_url}{pic_name}', auth = HTTPBasicAuth('butter', 'fly'))

# we have 500 server error...
print(response.status_code)

#with open(f'{pic_name}', 'wb') as fout:
#    fout.write(response.content)

# Check cookies
session = requests.Session()
response = session.get(url, auth = HTTPBasicAuth('butter', 'fly'))
print(session.cookies.get_dict())

#... Nothing

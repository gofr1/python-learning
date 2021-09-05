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

#* 200 !!
print(response.status_code)

with open(f'{pic_name}', 'wb') as fout:
    fout.write(response.content)

# Check cookies
session = requests.Session()
response = session.get(f'{standard_url}{pic_name}', auth = HTTPBasicAuth('butter', 'fly'))
print(session.cookies.get_dict())
#... Nothing

# Check headers
print(response.headers)
#* {
#*     'Content-Type': 'image/jpeg', 
#*     'Content-Range': 'bytes 0-30202/2123456789', 
#*     'Content-Length': '30203', 
#*     'Date': 'Sat, 04 Sep 2021 17:01:40 GMT', 
#*     'Server': 'lighttpd/1.4.55'
#* }

# The problem with picture is fixed!
# Hmm... we got 'Content-Range': 'bytes 0-30202/2123456789'
# Let's investigate further

headers = {"Range": "bytes=30203-30236"}
response = requests.get(f'{standard_url}{pic_name}', auth = HTTPBasicAuth('butter', 'fly'),headers=headers)
print(response.headers)
#* {
#*     'Content-Type': 'application/octet-stream', 
#*     'Content-Transfer-Encoding': 'binary', 
#*     'Content-Range': 'bytes 30203-30236/2123456789', 
#*     'Content-Length': '34', 
#*     'Date': 'Sun, 05 Sep 2021 07:54:47 GMT', 
#*     'Server': 'lighttpd/1.4.55'
#* }

with open(f'bin.txt', 'wb') as fout:
    fout.write(response.content)
# In the file you will see this message:
#* Why don't you respect my privacy?

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


headers = {"Range": "bytes=30347-30883"}
response = requests.get(f'{standard_url}{pic_name}', auth = HTTPBasicAuth('butter', 'fly'),headers=headers)
print(response.headers)

with open(f'bin2.txt', 'wb') as fout:
    fout.write(response.content)
#* we can go on in this way for really long time

import re

next_range = '30203-30236'
# Now we can write a loop to get all the text from content ranges:
while True:
    headers = {"Range": f"bytes={next_range}"}
    response = requests.get(f'{standard_url}{pic_name}', auth = HTTPBasicAuth('butter', 'fly'),headers=headers)
    bytesRegex = re.compile(r'[0-9]{1,8}-[0-9]{1,8}')
    print(response.headers)
    print(response.content)
    try:
        current_range = bytesRegex.search(response.headers['Content-Range']).group()
    except KeyError:
        print('no more ranges\n')
        break
    else:
        next_range = f'{(int(current_range.split("-")[1])+1)}-2123456789'
        print(response.headers)
        print(response.content)

#* b"Why don't you respect my privacy?\n"
#* b'we can go on in this way for really long time.\n'
#* b'stop this!\n'
#* b'invader! invader!\n'
#* b'ok, invader. you are inside now. \n'
#* no more ranges

# maybe it's "invader"?
response = requests.get(f'{standard_url}invader.html', auth = HTTPBasicAuth('butter', 'fly'))
print(response.headers)
#* {
#*     'Content-Type': 'text/html', 
#*     'Accept-Ranges': 'bytes', 
#*     'ETag': '"522821741"', 
#*     'Last-Modified': 'Sat, 12 Mar 2016 19:38:45 GMT', 
#*     'Content-Length': '17', 
#*     'Date': 'Sun, 05 Sep 2021 08:38:36 GMT', 
#*     'Server': 'lighttpd/1.4.55'
#* }
print(response.content)
#* Yes! that's you!
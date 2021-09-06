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

import re

next_range = '30203-30236'
while True:
    headers = {"Range": f"bytes={next_range}"}
    response = requests.get(f'{standard_url}{pic_name}', auth = HTTPBasicAuth('butter', 'fly'),headers=headers)
    bytesRegex = re.compile(r'[0-9]{1,8}-[0-9]{1,8}')
    overallRegex = re.compile(r'[0-9]{10}')
    try:
        current_range = bytesRegex.search(response.headers['Content-Range']).group()
        overall_range = overallRegex.search(response.headers['Content-Range']).group()
        content_length = int(response.headers['Content-Length'])
    except KeyError:
        print('no more ranges\n')
        break
    else:
        range_from = (int(current_range.split("-")[1])+1)
        range_to = range_from + content_length
        next_range = f'{range_from}-{range_to}'
        print(response.headers)
        print(str(response.content.decode('utf8')).strip())

#* b"Why don't you respect my privacy?\n"
#* b'we can go on in this way for really long time.\n'
#* b'stop this!\n'
#* b'invader! invader!\n'
#* b'ok, invader. you are inside now. \n'
#* no more ranges

# maybe it's "invader"?
invader = 'invader.html'
response = requests.get(f'{standard_url}{invader}', auth = HTTPBasicAuth('butter', 'fly'))
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


# Let's try to go over the other side of the range
headers = {"Range": f"bytes=2123456744-2123456788"}
response = requests.get(f'{standard_url}{pic_name}', auth = HTTPBasicAuth('butter', 'fly'),headers=headers)
print(response.headers)
print(response.content)
#* esrever ni emankcin wen ruoy si drowssap eht

content_str = str(response.content.decode('utf8')).strip()[::-1]
print(content_str)
#* the password is your new nickname in reverse

# Hmm.. password for what? 
# And what is a nickname? invader?
password = 'invader'[::-1]

# And password for what? Go further
headers = {"Range": f"bytes=2123456739-2123456743"}
response = requests.get(f'{standard_url}{pic_name}', auth = HTTPBasicAuth('butter', 'fly'),headers=headers)
print(response.headers)
print(response.content)
#* and it is hiding at 1152983631.

headers = {"Range": f"bytes=1152983631-0"}
response = requests.get(f'{standard_url}{pic_name}', auth = HTTPBasicAuth('butter', 'fly'),headers=headers)
print(response.headers)

with open('bin','wb') as fout:
    fout.write(response.content)

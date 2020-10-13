#12
#pip install GFX

from bs4 import BeautifulSoup, SoupStrainer
import requests
from io import BytesIO
from PIL import Image
from requests.auth import HTTPBasicAuth

standard_url = "http://www.pythonchallenge.com/pc/return/"
url = f"{standard_url}evil.html"
page = requests.get(url, auth = HTTPBasicAuth('huge', 'file'))
data = page.text
soup = BeautifulSoup(data)
picture_urls = []

for link in soup.find_all('img'):
    picture_urls.append(link.get('src'))

pic_name = picture_urls[0]
response = requests.get(f'{standard_url}{pic_name}', auth = HTTPBasicAuth('huge', 'file'))
img = Image.open(BytesIO(response.content))
img.save(f'{pic_name}')


for i in range(2,10):
    pic_name = ''.join(str(i) if c.isdigit() else c for c in pic_name)
    response = requests.get(f'{standard_url}{pic_name}', auth = HTTPBasicAuth('huge', 'file'))
    if response.text == 'Bert is evil! go back!\n':
        break
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.save(f'{pic_name}')

# evil2.jpg says: Not .jpg - .gfx so lets downolad evil2.gfx
response = requests.get(f'{standard_url}evil2.gfx', auth = HTTPBasicAuth('huge', 'file'))

with open("evil2.gfx", "wb") as f:
    f.write(response.content)

# there is 5 stacks lets split file by 5
data = open("evil2.gfx", "rb").read()

for i in range(5):
    open('%d.jpg' % i ,'wb').write(data[i::5])

data.close()
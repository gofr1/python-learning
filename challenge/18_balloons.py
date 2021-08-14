#18
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
from io import BytesIO
from PIL import Image

standard_url = "http://www.pythonchallenge.com/pc/return/"
url = f"{standard_url}balloons.html"
response = requests.get(url, auth = HTTPBasicAuth('huge', 'file'))
page_contents = BeautifulSoup(response.text, 'html.parser')

print(page_contents)

# get all pictures
picture_urls = []

for link in page_contents.find_all('img'):
    picture_urls.append(link.get('src'))

# take the only one
pic_name = picture_urls[0]

# and get it
response = requests.get(f'{standard_url}{pic_name}', auth = HTTPBasicAuth('huge', 'file'))
img = Image.open(BytesIO(response.content))
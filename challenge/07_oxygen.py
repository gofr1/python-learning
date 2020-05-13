# 7
from bs4 import BeautifulSoup, SoupStrainer
import requests
from io import BytesIO


standard_url = "http://www.pythonchallenge.com/pc/def/"

url = f"{standard_url}oxygen.html"
page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data)
picture_urls = []

for link in soup.find_all('img'):
    picture_urls.append(link.get('src'))

for picture_url in picture_urls:
    response = requests.get(f'{standard_url}{picture_url}')

img = response.content

byte_io = BytesIO(img)

# 7
from bs4 import BeautifulSoup, SoupStrainer
import requests
from io import BytesIO
from PIL import Image

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

    img = Image.open(BytesIO(response.content))
    img_size = img.size
    l = ''
    y = img_size[1]//2

    for x in range(0,img_size[0],7):
        r, b, g, a = img.getpixel((x, y))
        if r==b==g:
            l += chr(r)
    
    print(l)
    
    answer = l[(len(l)-1)//2:-1]
    result = ''
    for symbol in answer.split(','):
        result += chr(int(symbol))
    
    print(result)


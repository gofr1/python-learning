from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
from io import BytesIO
from PIL import Image


standard_url = "http://www.pythonchallenge.com/pc/return/"
url = f"{standard_url}italy.html"
response = requests.get(url, auth = HTTPBasicAuth('huge', 'file'))
page_contents = BeautifulSoup(response.text, 'html.parser')

picture_urls = []

for link in page_contents.find_all('img'):
    picture_urls.append(link.get('src'))
    new_img_size = (link.get('width'), link.get('height'))

pic_name = picture_urls[1]
new_img_size = (int(new_img_size[0]), int(new_img_size[1]))

response = requests.get(f'{standard_url}{pic_name}', auth = HTTPBasicAuth('huge', 'file'))
img = Image.open(BytesIO(response.content))
img_size = img.size

new_img = Image.new('RGB', new_img_size, color = 'white')

def get_pixels():
    """Get pixels from original file"""
    x = 0
    while x < img_size[0]:
        yield img.getpixel((x,0))
        x += 1

def where_to():
    """Should switch direction"""
    where_to_go = [(1,0),(0,1),(-1,0),(0,-1)]
    while True:
        g = where_to_go.pop(0)
        yield g
        where_to_go.append(g)

def steps():
    """"Get x,y in spiral way
    0,0 -> right -> down -> left -> up -> right ...
    """
    size = sum(new_img_size)
    turns = size//2 
    step = where_to()
    x, y = -1, 0 # x = -1 because we will use the next direction immediately 
    while turns >= 0:
        delta = next(step)
        for _ in range(turns):
            x, y = delta[0] + x, delta[1] + y
            yield (x,y)
        size -= 1
        turns = size//2 

pixels = get_pixels()
coordinates = steps()

for _ in range(img_size[0]):
    r,g,b = next(pixels)
    x,y = next(coordinates)
    new_img.putpixel((x,y),(r,g,b))

new_img.save('new_img.png')


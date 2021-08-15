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

# split images
img_size = img.size
left_img = Image.new('RGB', (img_size[0]//2,img_size[1]), color = 'white')
right_img = Image.new('RGB', (img_size[0]//2,img_size[1]), color = 'white')

for y in range(1,img_size[1]-1):
    for x in range(1,img_size[0]-1):
        r,g,b = img.getpixel((x,y))
        if x < img_size[0]//2:
            left_img.putpixel((x,y),(r,g,b))
        else:
            xr = x - img_size[0]//2
            right_img.putpixel((xr,y),(r,g,b))

# save images to check
left_img.save('left_img.png')
right_img.save('right_img.png')
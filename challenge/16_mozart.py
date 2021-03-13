from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
from io import BytesIO
from PIL import Image


standard_url = "http://www.pythonchallenge.com/pc/return/"
url = f"{standard_url}mozart.html"
response = requests.get(url, auth = HTTPBasicAuth('huge', 'file'))
page_contents = BeautifulSoup(response.text, 'html.parser')

picture_urls = []

for link in page_contents.find_all('img'):
    picture_urls.append(link.get('src'))

pic_name = picture_urls[0]
response = requests.get(f'{standard_url}{pic_name}', auth = HTTPBasicAuth('huge', 'file'))
img = Image.open(BytesIO(response.content))
img_size = img.size

# get all the pixels
x, y = 0, 0
pixels = []

while y < img_size[1]:
    while x < img_size[0]:
        pixels.append([x, y, img.getpixel((x,y))])
        x += 1
    x = 0
    y += 1

# find shifts
row = []
rows = []

for pixel in pixels:
    row.append(pixel)
    if (pixel[2] == 195 or pixel[0] == img_size[0]-1) and len(row) > 4:
        rows.append(row)
        row = []

# save image into a new file with shifting
new_img = Image.new('P', img_size)
x, y = 0, 0
row = []
for i in range(0,len(rows)-1,2):
    row.append(rows[i+1])
    row.append(rows[i])
    for r in row:
        for dot in r:
            new_img.putpixel((x,y),dot[2])
            x += 1
    x = 0
    y += 1
    row = []

new_img.save(pic_name)
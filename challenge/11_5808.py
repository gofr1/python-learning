#11
from bs4 import BeautifulSoup, SoupStrainer
import requests
from io import BytesIO
from PIL import Image
from requests.auth import HTTPBasicAuth

standard_url = "http://www.pythonchallenge.com/pc/return/"
url = f"{standard_url}5808.html"
page = requests.get(url, auth = HTTPBasicAuth('huge', 'file'))
data = page.text
soup = BeautifulSoup(data)
picture_urls = []

for link in soup.find_all('img'):
    picture_urls.append(link.get('src'))

for picture_url in picture_urls:
    response = requests.get(f'{standard_url}{picture_url}', auth = HTTPBasicAuth('huge', 'file'))

    img = Image.open(BytesIO(response.content))
    img_size = img.size
    
    new_img = Image.new('RGB', img_size, color = 'white')

    for x in range(0,img_size[0]-2,2):
        for y in range(0,img_size[1]-2,2):
            r,g,b = img.getpixel((x,y))
            new_img.putpixel((x,y),(r,g,b))
    
    for x in range(1,img_size[0]-2,2):
        for y in range(1,img_size[1]-2,2):
            r,g,b = img.getpixel((x,y))
            new_img.putpixel((x,y),(r,g,b))

    newsize = (320, 240) 
    new_img = new_img.resize(newsize) 
    new_img.save('new_img.png')
    
    # Shows the image in image viewer  
    new_img.show()  
    
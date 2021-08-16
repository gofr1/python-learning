#18
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
from io import BytesIO
from PIL import Image, ImageChops 

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
img.save('orig_img.png')

# split images
img_size = img.size
x_size = img_size[0]//2
y_size = img_size[1]

left_img = Image.new('RGB', (x_size,y_size), color = 'white')
right_img = Image.new('RGB', (x_size,y_size), color = 'white')

for y in range(1,y_size-1):
    for x in range(1,img.size[0]-1):
        r,g,b = img.getpixel((x,y))
        if x < x_size:
            left_img.putpixel((x,y),(r,g,b))
        else:
            xr = x - x_size 
            right_img.putpixel((xr,y),(r,g,b))

# save images to check
left_img.save('left_img.png')
right_img.save('right_img.png')

# find difference
both_img = Image.new('RGB', (x_size,y_size), color = 'white')

for x in range(1,x_size-1):
   for y in range(1,y_size-1):
        rl,gl,bl = left_img.getpixel((x,y))
        rr,gr,br = right_img.getpixel((x,y))
        #if x < 20 and y< 20:
        #    print(rl,gl,bl)
        #    print(rr,gr,br)
        r,g,b = (rl-rr), (gl-gr), (bl-br)
        #print(r,g,b)
        both_img.putpixel((x,y),(r,g,b))

both_img.save('both_img.png')

# finding difference with ImageChops
diff = ImageChops.difference(right_img, left_img) 
  
# showing the difference 
diff.show()
diff.save('both_img.png') 
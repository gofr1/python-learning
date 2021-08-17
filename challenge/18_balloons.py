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

# This method is used to get the mode (bands) present in an image.
print(f'Bands: {Image.Image.getbands(img)}')
# Gets the minimum and maximum pixel values for each band in the image.
print(f'Extrema: {Image.Image.getextrema(img)}')

# split images
img_size = img.size
x_size = img_size[0]//2
y_size = img_size[1]

left_img = Image.new('RGB', (x_size,y_size), color = 'white')
right_img = Image.new('RGB', (x_size,y_size), color = 'white')

for y in range(0,y_size):
    for x in range(0,img.size[0]):
        r,g,b = img.getpixel((x,y))
        if x < x_size:
            left_img.putpixel((x,y),(r,g,b))
        else:
            xr = x - x_size 
            right_img.putpixel((xr,y),(r,g,b))

# save images to check
left_img.save('left_img.png')
right_img.save('right_img.png')

print(f'Bands: {Image.Image.getbands(left_img)}')
print(f'Extrema: {Image.Image.getextrema(left_img)}')

print(f'Bands: {Image.Image.getbands(right_img)}')
print(f'Extrema: {Image.Image.getextrema(right_img)}')

# Extrema looks different
# Let's use extrema diff to cretae a diffrenet picture with delta for each color

left_ex = Image.Image.getextrema(left_img)
right_ex = Image.Image.getextrema(right_img)
ex = []

for i in range(3):
    ex.append(left_ex[i][1] - right_ex[i][1])

print(ex)

# use delta 
ex_img = Image.new('RGB', (x_size,y_size), color = 'white')

for x in range(0,x_size):
   for y in range(0,y_size):
        rl,gl,bl = right_img.getpixel((x,y))
        r,g,b = (rl+ex[0]), (gl+ex[0]), (bl+ex[2])
        #print(r,g,b)
        ex_img.putpixel((x,y),(r,g,b))

ex_img.save('ex_img.png') 


# find difference in manual way with loops
both_img = Image.new('RGB', (x_size,y_size), color = 'white')

for x in range(0,x_size):
   for y in range(0,y_size):
        rl,gl,bl = left_img.getpixel((x,y))
        rr,gr,br = right_img.getpixel((x,y))
        r,g,b = (rl-rr), (gl-gr), (bl-br)
        #print(r,g,b)
        both_img.putpixel((x,y),(r,g,b))

both_img.save('both_img.png') 

# let's try finding difference with ImageChops
diff = ImageChops.difference(right_img, left_img) 
#diff = diff.convert('RGBA')

# showing & saving the difference 
# diff.show()
diff.save('both_img.png') 


# Hm... <!-- it is more obvious that what you might think -->
# the difference is brightness! Let's try:

url = f"{standard_url}brightness.html"
response = requests.get(url, auth = HTTPBasicAuth('huge', 'file'))
page_contents = BeautifulSoup(response.text, 'html.parser')

print(page_contents)

# <!-- maybe consider deltas.gz -->

url = f"{standard_url}deltas.gz"
gz_content = requests.get(url, auth = HTTPBasicAuth('huge', 'file')).content

with open('deltas.gz', 'wb') as fout:
    fout.write(gz_content)
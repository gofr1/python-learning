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

gz_filename = 'deltas.gz'

url = f"{standard_url}{gz_filename}"
gz_content = requests.get(url, auth = HTTPBasicAuth('huge', 'file')).content

with open(gz_filename, 'wb') as fout:
    fout.write(gz_content)

# Now we have a file
import gzip

with gzip.open(gz_filename, 'r') as f:
    file_content = f.read()

for string in str(file_content).split('\\n'):
    print(string)

# Guess there is to parts in file, let's get them

bytes_string_left = ''
bytes_string_right = ''
i=0

for string in str(file_content).split('\\n'):
    len_string = len(string)
    bytes_string_left += string[0:len_string//2].strip() +' '
    bytes_string_right += string[-len_string//2:].strip() +' '
    if i == 0:
        bytes_string_left = bytes_string_left[2:] + ' '
    i+=1

with open('sample_left.png', 'wb') as fout:
    fout.write(bytearray.fromhex(bytes_string_left[0:-2]))

with open('sample_right.png', 'wb') as fout:
    fout.write(bytearray.fromhex(bytes_string_right[0:-2]))

# But guess it is not the thing, images are incomplete
# Let's try to check the differences and write in different files

bytes_left = []
bytes_right = []
i=0

for string in str(file_content).split('\\n'):
    len_string = len(string)
    bytes_string_left = string[:len_string//2].strip() 
    bytes_string_right = string[len_string//2:].strip()
    if i == 0:
        bytes_string_left = bytes_string_left[2:]
    i+=1
    bytes_left.append(bytes_string_left)
    bytes_right.append(bytes_string_right)

bytes_all = zip(bytes_left[:-1], bytes_right[:-1])
bytes_one = ''
bytes_two = ''
bytes_three = ''
# 1 that is in left but not in right
# 2 file is in right but not in left
# 3 are in both files
for ba in bytes_all:
    if ba[0] == ba[1]:
        bytes_three += ba[0] + ' '
        bytes_one += ba[0] + ' ' 
        bytes_two += ba[1] + ' ' 
    else:
        #if ba[0] == '':
        #    bytes_two += ba[1] + ' '
        #elif ba[1] == '':
        #    bytes_one += ba[0] +' '
        #else:           
        bytes_one += ba[0] + ' ' 
        bytes_two += ba[1] + ' ' 
        #print(f'"{ba[0]}","{ba[1]}')

with open('1.png', 'wb') as fout:
    fout.write(bytearray.fromhex(bytes_one))

with open('2.png', 'wb') as fout:
    fout.write(bytearray.fromhex(bytes_two))

with open('3.png', 'wb') as fout:
    fout.write(bytearray.fromhex(bytes_three))

# Not that good
# Let's use difflib

data = gzip.open(gz_filename)
left_part, right_part = [], []

for string in data:
    left_part.append(string[:53].decode()+"\n")
    right_part.append(string[56:].decode())

data.close()

import difflib

#? Each line of a Differ delta begins with a two-letter code:
#? 
#? '- ' line unique to sequence 1
#? '+ ' line unique to sequence 2
#? '  ' line common to both sequences
#? '? ' line not present in either input sequence

compare = difflib.Differ().compare(left_part, right_part)

# check what is inside
from pprint import pprint

pprint(list(compare))

# '  2f 17 a4 5d 8e 74 86 c9 02 d3 98 e6 09 62 99 43 ae 50\n',
# '+ 1a 0c 06 83 11 a8 c1 60 30 18 81 1a 0c 06 83 11 a8 c1\n',
# '  d5 54 89 24 56 8e ac 46 2d b1 d9 a2 ce 38 4d 91 30 78\n',
# '- 08 84 40 05 02 81 40 08 54 20 10 08 84 40 05 02 81 40\n',
# '  86 49 8d fa cb 3a 79 2b 2d da 30 50 14 45 51 60 60 7c\n',

f1 = open('1.png', 'wb')
f2 = open('2.png', 'wb')
f3 = open('3.png', 'wb')

for line in compare:
    bs = bytes([int(p, 16) for p in line[2:].strip().split(' ') if p])
    if line[0] == '+':
        f2.write(bs)
    elif line[0] == '-':
        f3.write(bs)
    else:
        f1.write(bs)

f1.close()
f2.close()
f3.close()

# ../hex/bin.html - back one level (from "return") and go "hex/bin.html")
# butter - login
# fly - password

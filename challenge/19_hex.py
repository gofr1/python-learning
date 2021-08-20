#19
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
from io import BytesIO
from PIL import Image, ImageChops 

standard_url = "http://www.pythonchallenge.com/pc/hex/"
url = f"{standard_url}bin.html"
response = requests.get(url, auth = HTTPBasicAuth('butter', 'fly'))
page_contents = BeautifulSoup(response.text, 'html.parser')

print(str(page_contents)[0:643])

#* Content-type: audio/x-wav; name="indian.wav"
#* Content-transfer-encoding: base64

# And further goes base64 string

import base64

base64_message = str(page_contents)[645:151431]
base64_bytes = base64_message.encode('utf8')
message_bytes = base64.b64decode(base64_bytes)

with open('indian.wav','wb') as fout:
    fout.write(message_bytes)

# Play the file
from playsound import playsound
playsound('indian.wav')

# wav file says 'sorry!'
# Lets try sorry.html

url = f"{standard_url}sorry.html"
response = requests.get(url, auth = HTTPBasicAuth('butter', 'fly'))
page_contents = BeautifulSoup(response.text, 'html.parser')

print(page_contents)
#* - "what are you apologizing for?"
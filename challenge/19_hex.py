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

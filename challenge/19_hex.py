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


# Let's play with wave module
import wave

indian =  wave.Wave_read('indian.wav')
print(f'Number of channels: {indian.getnchannels()}')
print(f'Sample width: {indian.getsampwidth()}')
print(f'Frame rate: {indian.getframerate()}')
print(f'Number of frames: {indian.getnframes()}')
print(f'parameters: {indian.getparams()}')

new = wave.Wave_write('new.wav')
new.setframerate(11025)
new.setsampwidth(2)
new.setnframes(55788//2)
new.setnchannels(1)

print(f'Number of channels: {new.getnchannels()}')
print(f'Sample width: {new.getsampwidth()}')
print(f'Frame rate: {new.getframerate()}')
print(f'Number of frames: {new.getnframes()}')
print(f'parameters: {new.getparams()}')

data = indian.readframes(55788)

new.writeframes(data)

indian.close()
new.close()

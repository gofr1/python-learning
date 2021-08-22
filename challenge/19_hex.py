#19
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth

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
print(f'''Number of channels: {indian.getnchannels()}'
Sample width: {indian.getsampwidth()}
Frame rate: {indian.getframerate()}
Number of frames: {indian.getnframes()}''')

# use parameters: .getparams()} to get al once

new = wave.Wave_write('new.wav')
new.setframerate(11025*2) # increase frame rate
new.setsampwidth(1) # decrease sample width
new.setnframes(55788)
new.setnchannels(1)

print(f'''Number of channels: {new.getnchannels()}
Sample width: {new.getsampwidth()}
Frame rate: {new.getframerate()}
Number of frames: {new.getnframes()}''')

# write data from one file to another
data = indian.readframes(55788)

# write audio frames and make sure nframes is correct.
new.writeframes(data)

# close files
indian.close()
new.close()

# play sound
playsound('new.wav')

#* Yoy are an idiot, a-ha aha-ha...
# :) let's check idiot.html

standard_url = "http://www.pythonchallenge.com/pc/hex/"
url = f"{standard_url}idiot.html"
response = requests.get(url, auth = HTTPBasicAuth('butter', 'fly'))
page_contents = BeautifulSoup(response.text, 'html.parser')

print(page_contents)

#* <img border="0" src="../stuff/leopold.jpg"/><br/><br/>
#*         "Now you should apologize..."<br/>
#* <br/><a href="idiot2.html">Continue to the next level</a>
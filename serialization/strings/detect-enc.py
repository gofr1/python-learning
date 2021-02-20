# sudo pip3 install chardet
# curl -G https://raw.githubusercontent.com/LinkedInLearning/python-serialization-2822693/master/Ch06/06_05/aow.txt > aow.txt
# curl -G https://raw.githubusercontent.com/LinkedInLearning/python-serialization-2822693/master/Ch06/06_05/aow16.txt > aow16.txt

import chardet

with open('aow.txt', 'rb') as fp:
    data = fp.read()

chardet.detect(data)
#* {'encoding': 'UTF-8-SIG', 'confidence': 1.0, 'language': ''}

with open('aow16.txt', 'rb') as fp:
    data16 = fp.read()

chardet.detect(data16)
#* {'encoding': 'UTF-16', 'confidence': 1.0, 'language': ''}
#!/usr/bin/env python3

# gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate text-to-speech API
# sudo pip3 install gtts

from io import BytesIO
from pygame import mixer
from gtts import gTTS

def speak(text):
    with BytesIO() as f:
        gTTS(text=text, lang="en").write_to_fp(f)
        f.seek(0)

        mixer.init()
        mixer.music.load(f)
        mixer.music.play()
        while mixer.music.get_busy():
            continue

if __name__ == '__main__':
    text = input("What should I say? >>")
    speak(text)
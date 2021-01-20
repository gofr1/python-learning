#!/usr/bin/env python3

# sudo pip3 install pyqt5
# sudo pip3 install pyperclip

# Enables cross-platform copy-pasting in Python which was earlier absent
import pyperclip 

pyperclip.copy("Hello world !") # copy to the clipboard
pyperclip.paste() # paste from clipboard
  
pyperclip.copy("Isn't pyperclip fascinating?") 
pyperclip.paste()


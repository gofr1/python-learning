#!/usr/bin/env python3

#  sudo pip install pyautogui
# On Linux, additionally you need to install the scrot application, as well as Tkinter:
#     sudo apt-get install scrot
#     sudo apt-get install python3-tk
#     sudo apt-get install python3-dev
# PyAutoGUI install the modules it depends on, including PyTweening, PyScreeze, PyGetWindow, PymsgBox, and MouseInfo.

import pyautogui

wh = pyautogui.size() # Obtain the screen resolution.
wh
#* Size(width=1920, height=1080)

wh[0]
#* 1920

print(f'Height: {wh.height}')
#* Height: 1080
print(f'Width: {wh.width}')
#* Width: 1920

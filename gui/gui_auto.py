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

# Move the mouse to left-top corner and do the squares
for i in range(4): # Move mouse in a square.
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

# Move the mouse in current position
for i in range(4):
    pyautogui.move(100, 0, duration=0.25)   # right
    pyautogui.move(0, 100, duration=0.25)   # down
    pyautogui.move(-100, 0, duration=0.25)  # left
    pyautogui.move(0, -100, duration=0.25)  # up

# Get mouse position
pyautogui.position() # Get current mouse position.
#* Point(x=717, y=586)

pyautogui.position() # Get current mouse position again.
#* Point(x=801, y=688)
p = pyautogui.position() # And again.
p
#* Point(x=756, y=665)

p[0] # The x-coordinate is at index 0. y - 1
#* 756
p.x # The x-coordinate is also in the x attribute. p.y
#* 756
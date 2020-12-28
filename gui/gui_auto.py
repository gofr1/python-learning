#!/usr/bin/env python3

#  sudo pip install pyautogui
# On Linux, additionally you need to install the scrot application, as well as Tkinter:
#     sudo apt-get install scrot
#     sudo apt-get install python3-tk
#     sudo apt-get install python3-dev
# PyAutoGUI install the modules it depends on, including PyTweening, PyScreeze, PyGetWindow, PymsgBox, and MouseInfo.

import pyautogui, time

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

# Clicking the mouse
pyautogui.click(756, 665) # Move mouse to (1756, 665) and click.

# Dragging the mouse
time.sleep(10)
pyautogui.click()    # Click to make the window active.
distance = 300
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)   # Move right.
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2)   # Move down.
    pyautogui.drag(-distance, 0, duration=0.2)  # Move left.
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2)  # Move up.

# if you open gimp and create file this script will draw
# something like spiral:
#* -------+
#* |+----+|
#* ||+--+||
#* |||--+||
#* ||+--+||
#* |+----+|
#* +------+

# Scrolling the mouse
# Passing a positive integer scrolls up, and passing a negative integer scrolls down.
pyautogui.scroll(50)
pyautogui.scroll(-50)


# Getting a screenshot (require scrot)
# These functions can also return a Pillow Image object of the current screen’s appearance.
im = pyautogui.screenshot()
im
#* <PIL.PngImagePlugin.PngImageFile image mode=RGB size=1920x1080 at 0x7FE6414E37F0>

# You can obtain the RGB color value of a particular pixel on the screen with the pixel() function.
pyautogui.pixel(50, 200)
#* RGB(red=41, green=40, blue=54)

# pixelMatchesColor() function will return True if the pixel at 
# the given x- and y-coordinates on the screen matches the given color.
pyautogui.pixelMatchesColor(50, 200, (41, 40, 54))
#* True
pyautogui.pixelMatchesColor(50, 200, (100, 54, 24))
#* False
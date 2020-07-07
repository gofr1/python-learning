from tkinter import Tk, Canvas

root = Tk()

# creating a canvas
canvas = Canvas(root)
canvas.pack()
canvas.config(width=640, height=480)

# create a line
line = canvas.create_line(160, 360, 480, 120, width=5, fill='blue')

# cnange line property
canvas.itemconfigure(line, fill='green')

# get coordinates
canvas.coords(line) # [160.0, 360.0, 480.0, 120.0]

# change coordinates
canvas.coords(line, 0, 0, 320, 240, 640, 0)

# add some smooth
canvas.itemconfigure(line, smooth=True)
canvas.itemconfigure(line, splinesteps=5)
canvas.itemconfigure(line, splinesteps=100)

# remove line
canvas.delete(line)

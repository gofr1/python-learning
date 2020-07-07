from tkinter import Tk, Canvas, PhotoImage, Button

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

# draw a rectangle
rect = canvas.create_rectangle(160, 120, 480, 360)

# change properties
canvas.itemconfigure(rect, fill='yellow')

# draw an oval and an arc
oval = canvas.create_oval(160, 120, 480, 360)
arc = canvas.create_arc(160, 1, 480, 240)

canvas.itemconfigure(arc, fill='green', start=0, extent=180)

# and polygon (triangle)
poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill='blue')

# adding text
text = canvas.create_text(320, 240, text='Python', font=('Verdana', 32, 'bold'))

# adding image
logo = PhotoImage(file='../../Pictures/img/python_logo.gif')
image = canvas.create_image(320, 240, image=logo)

# lift/lower some items
canvas.lift(text)
canvas.lower(image) # now image is under all objects 
# lets move it under the text
canvas.lower(image, text)

# we can add another objects
button = Button(canvas, text='Click Me')
canvas.create_window(320, 60, window=button)

# adding tags
canvas.itemconfigure(rect, tag=('shape'))
canvas.itemconfigure(oval, tag=('shape', 'round'))

# refering to objects with tags
canvas.itemconfigure('shape', fill='grey')

# get tags of an item
canvas.gettags(oval)
from tkinter import Tk,CENTER,PhotoImage
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text='Hello, Tkinter!')
label.pack()

# wrapping long text
label.config(text='Howdy, Tkinter! It\'s been a while since we last met. Great to see you again!')
label.config(wraplength=150) # in pixels

# justify text
label.config(justify=CENTER)

# changing foreground
label.config(foreground='blue')

# changing background
label.config(background='yellow')

# font properties
label.config(font=('Verdana', 14, 'bold'))

# adding image to a label
# accepts GIF, PGM or PPM files
label.config(text='Howdy, Tkinter!')
logo = PhotoImage(file='../../Pictures/img/python_logo.gif')
label.config(image=logo) 

# to store image properly better use
label.img = logo
label.config(image=label.img) # will stick around as long as label exists

# label has text and image properties
# we can switch between then using compound
label.config(compound='text')

# or we can display both
label.config(compound='left') # center, bottom, top, left, right
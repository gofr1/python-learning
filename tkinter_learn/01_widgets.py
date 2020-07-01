from tkinter import Tk, Label
from tkinter import ttk

root = Tk()
button = ttk.Button(root, text = 'Click Me')
button.pack()

# to access button properties
button['text']
button['text'] = 'Press Me'
button.config(text = 'Push Me')

# will show all
button.config()

# unique identifier of a widget
str(button) # '.12345678'
str(root) # '.'

Label(root, text='Hello, Tkinter!').pack()


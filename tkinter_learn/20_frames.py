from tkinter import Tk, RIDGE
from tkinter import ttk

# create a form 
root = Tk()
frame = ttk.Frame(root)
frame.pack()

# by default frame is sized 0x0
frame.config(height=100, width=200)

# add border
frame.config(relief = RIDGE)

# add some button
ttk.Button(frame, text='Click Me!').grid()

# now frame is sized as button so lets some padding
frame.config(padding=(30,15))

ttk.LabelFrame(root, height=100, width=200, text='My Frame').pack()
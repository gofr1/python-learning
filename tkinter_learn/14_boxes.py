from tkinter import Tk, StringVar, Spinbox
from tkinter import ttk

# create a form 
root = Tk()
month = StringVar()
combobox = ttk.Combobox(root, textvariable=month)
combobox.pack()

# Combobox
# add values
combobox.config(values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# check selected value
month.get()

# set value
month.set('Oct')

# Spinbox
year = StringVar()
spinbox = Spinbox(root, from_=1984, to=2084, textvariable=year)
spinbox.pack()

# get a value
year.get()

# set a value
year.set(1500)
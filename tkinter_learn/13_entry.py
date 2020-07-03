from tkinter import Tk, END
from tkinter import ttk

# create a form and entry field
root = Tk()
entry = ttk.Entry(root, width=30)
entry.pack()

# check the value in an entry
entry.get()

# to delete symbols from entered string
entry.delete(0,1) # will remove 'H'

# to remove all
entry.delete(0, END)

# to insert the same syntax is used
entry.insert(0, 'Enter the password')

# to hide input
entry.config(show='*')

# states
entry.state(['disabled']) # off
entry.state(['!disabled']) # on

entry.state(['readonly']) # can copy text

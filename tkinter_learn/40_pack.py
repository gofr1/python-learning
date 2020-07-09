#!/usr/bin/env python3

from tkinter import Tk, mainloop, X, Y, BOTH, LEFT, BOTTOM
from tkinter import ttk

root = Tk()
ttk.Label(root, text='Hello, Tkinter!', background='yellow').pack(fill=X)
ttk.Label(root, text='Hello, Tkinter!', background='green').pack(fill=BOTH, expand=True, side=LEFT)
ttk.Label(root, text='Hello, Tkinter!', background='blue').pack(side=LEFT, anchor='nw', padx=10, pady=10)
ttk.Label(root, text='Hello, Tkinter!', background='red').pack(side=BOTTOM, ipadx=10, ipady=10)

label = ttk.Label(root, text='Hello, Tkinter!', background='grey').pack()
print(label) # that will return None
# better call pack method separately:
label1 = ttk.Label(root, text='Hello, Tkinter!', background='violet')
label1.pack()
print(label1) # that will return .!labelN
# and we could reference that label with the help of variable

for widget in root.pack_slaves(): # get all widgets in root window
    widget.pack_configure(fill=BOTH, expand=True) # change pack properties
    print(widget.pack_info()) # get pack widgit properties

label1.pack_forget()
label.pack_forget() # this will not be removed

root.mainloop()
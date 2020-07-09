#!/usr/bin/env python3

from tkinter import Tk, mainloop
from tkinter import ttk

root = Tk()
label1 = ttk.Label(root, text='Yellow', background='yellow')
label2 = ttk.Label(root, text='Blue', background='blue')
label3 = ttk.Label(root, text='Green', background='green')
label4 = ttk.Label(root, text='Orange', background='orange')

#   |   0   |   1   |
# 0 | Green | Orange|
# 1 | Blue  | Yellow|
label1.grid(row=1, column=1)
label2.grid(row=1, column=0)
label3.grid(row=0, column=0)
label4.grid(row=0, column=1)

#   |   0   |   1   |   2   |
# 0 | Green | Orange| Yellow|
# 1 |     Blue      |       |
label1.grid_configure(row=0, column=2, rowspan=2)
label2.grid_configure(row=1, column=0, columnspan=2)
label3.grid_configure(row=0, column=0)
label4.grid_configure(row=0, column=1)

# sticky labels :)
label1.grid_configure(stick='nsew')
label2.grid_configure(stick='e')
label3.grid_configure(stick='nsew')
label4.grid_configure(stick='nsew')

# to resize automaticaly when parent widget is resized
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)
root.columnconfigure(2, weight=1)

# add padding
label3.grid_configure(padx=10, pady=10)
label4.grid_configure(ipadx=25, ipady=25)

root.mainloop()
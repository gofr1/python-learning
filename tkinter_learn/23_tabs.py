from tkinter import Tk
from tkinter import ttk

# create a form with tab notebook
root = Tk()
notebook = ttk.Notebook(root)
notebook.pack()
# by default notebook is sized 0x0
# lets add frames
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text='One') # index 0
notebook.add(frame2, text='Two') # index 1

# lets add button
ttk.Button(frame1, text='Click Me!').pack()
# notice that both frames are resized by button size

# lets insert more tabs
frame3 = ttk.Frame(notebook)
notebook.insert(1, frame3, text='Three') # use indexing

# to remove by index 
notebook.forget(1)

# and add again in the end
notebook.add(frame3, text='Three') # index 0

# check what tab is selected
notebook.select()
notebook.index(notebook.select()) # to whow index

# to select tab programatically
notebook.select(0) # by index

# to change a state of a tabs
notebook.tab(1,state='disabled')

# to hide tab
notebook.tab(1,state='hidden')

# get tab back
notebook.tab(1,state='normal')

# get the properties of a tab
notebook.tab(0, 'text')
notebook.tab(0) # to see all properties

# to destroy root window with all childs and widgets 
root.destroy()
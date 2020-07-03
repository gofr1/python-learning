from tkinter import Tk, HORIZONTAL, BOTH, SUNKEN
from tkinter import ttk

# create a form with panned window
root = Tk()
panedwindow = ttk.Panedwindow(root, orient=HORIZONTAL)
panedwindow.pack(fill=BOTH, expand=True)

# by default panned window is sized 0x0
# so lets add frames
frame1 = ttk.Frame(panedwindow, width=100, height=300, relief=SUNKEN) # 0 index
frame2 = ttk.Frame(panedwindow, width=400, height=400, relief=SUNKEN) # 1 index

# adding frames
panedwindow.add(frame1, weight=1)
panedwindow.add(frame2, weight=4) # this frame will be expand 4 times that frame 1

# add one more frame
frame3 = ttk.Frame(panedwindow, width=50, height=400, relief=SUNKEN)
panedwindow.insert(1, frame3) # insert in 1 index
# this inserted frame will have weight = 0 by default and would not be resized

# to remove frame we can use forget method with index number
panedwindow.forget(1)

# to destroy root window with all childs and widgets 
root.destroy()
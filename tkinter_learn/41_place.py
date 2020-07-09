from tkinter import Tk, mainloop
from tkinter import ttk

root = Tk()
root.geometry('640x480+200+200') # size of window and pixels from top-left corner of the screen

label1 = ttk.Label(root, text='Yellow', background='yellow')
label2 = ttk.Label(root, text='Blue', background='blue')
label3 = ttk.Label(root, text='Green', background='green')
label4 = ttk.Label(root, text='Orange', background='orange')

label1.place(x=100, y=50) # pixels from top-left corner of the root window
label2.place(relx=0.5, rely=0.5) # from 0 to 1 a percentage from top-left corner of the root window 
# but Blue label is not in the center if window is resized 
label2.place(anchor='center') # also can use nsew

# if you use relative in absolute coordinates 
# at first relative will be calculated and absolute will be added above
label3.place(relx=0.5, rely=0.5, x=100, y=50)

# we can use negative coordinates
label4.place(relx=1.0, x=-5, y=5, anchor='ne')

# cange size
label1.place_configure(width=100, height=50)
label2.place_configure(relwidth=0.5, relheight=0.5)

root.mainloop()
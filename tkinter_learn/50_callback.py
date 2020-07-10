from tkinter import Tk, mainloop
from tkinter import ttk

def callback(number):
    print(number)

root = Tk()

# we need lambda elseway the standard call will not be working
button0 = ttk.Button(root, text='1', command=lambda: callback(1))
button1 = ttk.Button(root, text='2', command=lambda: callback(2))
button2 = ttk.Button(root, text='3', command=lambda: callback(3))

button0.pack()
button1.pack()
button2.pack()

root.mainloop()
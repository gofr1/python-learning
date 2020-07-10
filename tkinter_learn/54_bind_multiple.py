from tkinter import Tk, mainloop
from tkinter import ttk

root = Tk()

label0 = ttk.Label(root, text='Label 0')
label1 = ttk.Label(root, text='Label 1')

label0.pack()
label1.pack()

label0.bind('<ButtonPress>', lambda e: print('<ButtonPress> Label'))
label0.bind('<1>', lambda e: print('<1> Label'))

root.bind('<1>', lambda e: print('<1> Root'))
# in that case when left button click is binded both on label and root window
# now when you click on label0 both events will occur:
# <1> Label
# <1> Root

# so lets unbind left-click event from label
label0.unbind('<1>')
# now we will have
# <ButtonPress> Label
# <1> Root

root.bind_all('<Escape>', lambda e: print('Escape!!!'))

root.mainloop()
from tkinter import Tk, Frame, Label

root = Tk() # base window creation
root.title('It\'s me, label!') # window title
root.geometry("200x50") # window size

# lets create the frame inside a window
app = Frame(root)
app.grid()

# creation of a label inside a frame
lbl = Label(app, text = ("That's is it"))
lbl.grid()

# event loop
root.mainloop()
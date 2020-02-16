from tkinter import Tk, Frame, Button

root = Tk() # base window creation
root.title('Lazy buttons') # window title
root.geometry("200x95") # window size

# lets create the frame inside a window
app = Frame(root)
app.grid()

# creation of a butttons inside a frame
# first button
bttn1 = Button(app, text="I am doing nothing!")
bttn1.grid()

# second button
bttn2 = Button(app) 
bttn2.grid()
bttn2.configure(text="Me too") # we can change button properties with configure

# third button
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "And me!" # list like method of setting a propertie

# event loop
root.mainloop()
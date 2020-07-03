from tkinter import Tk, HORIZONTAL, DoubleVar
from tkinter import ttk

# create a form 
root = Tk()
progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progressbar.pack()

# indeterminate bar
progressbar.config(mode='indeterminate')
progressbar.start()
progressbar.stop()

# determinate bar
progressbar.config(mode='determinate', maximum=11.0, value=4.2)
progressbar.config(value=8.0)

progressbar.step()
# can enter number of steps to increment
progressbar.step(5) 
# but if number of steps exceed the maximum number
# the progress will start from the beginning

# use variable to change progress
value = DoubleVar()
progressbar.config(variable=value)

# lets use scale to change a progressbar
scale = ttk.Scale(root, orient=HORIZONTAL, length=400, from_=0.0, to=11.0, variable=value)
scale.pack()

# also we can change value programatically
scale.set(6.2)
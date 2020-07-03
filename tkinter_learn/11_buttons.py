from tkinter import Tk, PhotoImage, LEFT
from tkinter import ttk

# create a form and button
root = Tk()
button = ttk.Button(root, text='Click Me!')
button.pack()

# define a function to call when button is pressed
def callback():
    print('Clicked')

button.config(command=callback)

# invoke click
button.invoke()

# change state of a button
button.state(['disabled'])

# check state
button.instate(['disabled'])

# enable again
button.state(['!disabled'])

# can change appearance as labels
logo = PhotoImage(file='../../Pictures/img/python_logo.gif')
button.config(image=logo,compound = LEFT)

# lets make smaller logo
small_logo = logo.subsample(5,5)
button.config(image=small_logo)
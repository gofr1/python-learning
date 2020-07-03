from tkinter import Tk, StringVar
from tkinter import ttk

# create a form and check-button
root = Tk()
checkbutton = ttk.Checkbutton(root, text='SPAM?')
checkbutton.pack()

# wrappers variable classes are provided for 
# change tracking functionality
spam = StringVar()
spam.set('SPAM!')
spam.get()

checkbutton.config(variable=spam,onvalue='SPAM Please!',offvalue='Boo SPAM!')

# now lets click the button and check variable
spam.get()

# Radio buttons
breakfast = StringVar()
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value = 'SPAM').pack()
ttk.Radiobutton(root, text='Eggs', variable=breakfast, value = 'Eggs').pack()
ttk.Radiobutton(root, text='Sausage', variable=breakfast, value = 'Sausage').pack()
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value = 'SPAM').pack()

# try to click radio buttons and check variable
breakfast.get()

# textvariable
checkbutton.config(textvariable=breakfast)
# now when clicking radio buttons check button will be changed accordingly

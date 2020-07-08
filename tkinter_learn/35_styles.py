from tkinter import Tk
from tkinter import ttk

root = Tk()
button1 = ttk.Button(root, text='Button1')
button2 = ttk.Button(root, text='Button2')
button1.pack()
button2.pack()

# style
style = ttk.Style()

# check available themes
style.theme_names()

# what theme is currently used
style.theme_use()

# use another theme
style.theme_use('classic')
style.theme_use('default')

# check object styles
button1.winfo_class()

# change object style
style.configure('TButton', foreground='blue')

# create a new style for object
style.configure('Alarm.TButton', foreground='orange', font=('Arial', 24, 'bold'))

# an assign it to object
button2.config(style='Alarm.TButton')

# another way to change styles
style.map('Alarm.TButton', foreground=[('pressed', 'pink'), ('disabled', 'grey')])

# pressed button will be with font of a pink colour
# and disabled will be grey
button2.state(['disabled'])

# layout
style.layout('Alarm.TButton')
# layout options
style.element_options('Button.label')
# get current value of an option
style.lookup('Alarm.TButton', 'foreground')
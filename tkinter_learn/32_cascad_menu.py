from tkinter import Tk, Menu, PhotoImage, IntVar

root = Tk()
# this line tells Tk not to create terrible menu
root.option_add('*tearOff', False)

# create a menu
menubar = Menu(root)
root.config(menu=menubar)

# adding menu items (they are child of menu)
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)

menubar.add_cascade(menu=file, label='File')
menubar.add_cascade(menu=edit, label='Edit')
menubar.add_cascade(menu=help_, label='Help')

# lets add some commands in file menu
file.add_command(label='New', command= lambda: print('New File'))

# add separator
file.add_separator()

# add few more commands
file.add_command(label='Open...', command= lambda: print('Opening File...'))

# to add shortcuts (actualy just display it)
file.entryconfig('New', accelerator='Ctrl + N')

# add a picture
logo = PhotoImage(file='../../Pictures/img/python_logo.gif').subsample(10,10)
file.entryconfig('Open...', image=logo, compound='left')

# setting the states
file.entryconfig('Open...', state='disabled')

# delete
file.delete('Save')

# add sub-menu for save
save = Menu(file)
file.add_cascade(menu=save, label='Save')

save.add_command(label='Save As', command=lambda: print('Saving As...'))
save.add_command(label='Save All', command=lambda: print('Saving All...'))

# we can add a radio button (and other ones too)
choice = IntVar()
edit.add_radiobutton(label='One', variable=choice, value=1)
edit.add_radiobutton(label='Two', variable=choice, value=2)
edit.add_radiobutton(label='Three', variable=choice, value=3)

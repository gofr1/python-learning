from tkinter import Tk, PhotoImage
from tkinter import ttk

# create a form with treeview
root = Tk()
treeview = ttk.Treeview(root)
treeview.pack()

# add items on root node
treeview.insert('', '0', 'item1', text='First Item')
treeview.insert('', '1', 'item2', text='Second Item')
treeview.insert('', 'end', 'item3', text='Third Item')

logo = PhotoImage(file='../../Pictures/img/python_logo.gif').subsample(10,10)
treeview.insert('item2', 'end', 'python', text ='Python', image=logo)

# to show 5 items in view
treeview.config(height=5)

# to move items from one node to another
treeview.move('item2', 'item1', 'end')

# to open/close node programatically
treeview.item('item1', open=True)

# check property of the item
treeview.item('item1', 'open')

# to "remove" items
treeview.detach('item3')

# to get item back
treeview.move('item3', 'item2', '0')

# true delete of an item
treeview.delete('item3')

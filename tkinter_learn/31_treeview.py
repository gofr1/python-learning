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

# add one more column
treeview.config(columns=('version'))

# lets amend new column
treeview.column('version', width=50, anchor='center')
# and old one referencing it by index
treeview.column('#0', width=150)

# change heading
treeview.heading('version', text='Version')

# change values in new column
treeview.set('python', 'version', '3.8.3')

# add tags to an item in treeview
treeview.item('python', tags=('software'))

treeview.tag_configure('software', background='red') #not working

# check what item is selected
def callback(event):
    print(treeview.selection())

treeview.bind('<<TreeviewSelect>>', callback)

# by default you can select multiple items to change this
treeview.config(selectmode='browse') # allow to select 1 item at a time

# to add /remove items from selection
treeview.selection_add('python')
treeview.selection_remove('python')

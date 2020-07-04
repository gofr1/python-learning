from tkinter import Tk, Text, PhotoImage, Button

root = Tk()

# create a text widget
text = Text(root, width=40, height=10)
text.pack()

# wrapping
text.config(wrap='word')

# common base formats
# line.char 1.0 is the start
# end - the very end of text
# common modifiers
# +/-# char, +/-# line
# linestart, lineend, wordstart, wordend

text.get('1.0', 'end')
text.get('1.0', '1.end')

# inserting text 
text.insert('1.0 + 2 lines', 'Inserted message')
text.insert('1.0 + 2 lines lineend', ' and more\nand more...')

# deleting
text.delete('1.0') # only first symbol of first line
text.delete('1.0', '1.0 lineend') # will delete first line except last symbol \n
text.delete('1.0', '3.0 lineend + 1 chars') # will delete 1-3 lines + 1 char

# replacing
text.replace('1.0', '1.0 lineend', 'This is the first line.')

# states
text.config(state='disabled') # now you can't enter text
# delete/insert wont work

text.config(state='normal') 

# Tags are used to reference dections of the text
# 
# adding tags
text.tag_add('my_tag', '1.0', '1.0 wordend')
text.tag_configure('my_tag', background='yellow')
text.tag_remove('my_tag', '1.1', '1.3')

# to check tag range
text.tag_ranges('my_tag')

# get all tags
text.tag_names() # sel - is a selection special tag

# check tags on some area
text.tag_names('1.0')

# replacing with tags
text.replace('my_tag.first', 'my_tag.last', 'That')

# delete tag
text.tag_delete('my_tag')

# Marks

text.mark_names()

# insert special marked can be used to insert text in cursor position
# place cursor anyway in the text 
text.insert('insert', '_')

# placing a mark
text.mark_set('my_mark', 'end')

# where to put text before or behind the mark
text.mark_gravity('my_mark', 'right')

# to remove a mark
text.mark_unset('my_mark')

# add picture into text
image = PhotoImage(file='../../Pictures/img/python_logo.gif')
text.image_create('insert', image=image)

# or add button
button = Button(text, text='Click Me!')
text.window_create('insert', window=button)

root.destroy()
from tkinter import Tk, Text

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


from tkinter import Tk, mainloop
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root)
entry.pack()

# in that case it will use Ctrl+C and Ctrl+V events
entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

# to add your own event
entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))

# to view information about event
print(entry.event_info('<<OddNumber>>'))

# to genereate event programaticaly 
entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')

# to delete event
entry.event_delete('<<OddNumber>>')

root.mainloop()
from tkinter import Tk, mainloop
from tkinter import ttk

def key_press(event):
    print(f'type: {event.type}')
    print(f'widget: {event.widget}')
    print(f'char: {event.char}')
    print(f'keysym: {event.keysym}')
    print(f'keycode: {event.keycode}')
    print()

def shortcut(action):
    print(action)

root = Tk()

# Event format           | Description
# <Key>, <KeyPress>      | User pressed any key
# <KeyPress-Delete>      | User pressed Delete key (use keysym)
# <KeyRelease-Right>     | User released Right-Arrow key
# 1,2,3..a,b,c..         | User pressed a ...
# <space>, <less>...     | ... printable character
# <Shift_L>, <Control_L> | User pressed a special key
# <Return>               | User pressed the Enter key
# <Control-Alt-Next>     | User pressed key combination like Ctrl+Alt+PgDn
root.bind('<KeyPress>', key_press)

#  Remember the difference here, we can use lambda functions with the command callbacks,
# but for those we do not need to pass in a parameter, but when we use a lambda function 
# within the bind method, since the bind is passing that event object, we need to include 
# this additional variable here to capture that event object, or else we'll cause an error. 
root.bind('<Control-c>', lambda e: shortcut('Copy'))
root.bind('<Control-v>', lambda e: shortcut('Paste'))

root.mainloop()
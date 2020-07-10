from tkinter import Tk, mainloop, Canvas, LEFT, BOTH
from tkinter import ttk

def mouse_press(event):
    global prev
    prev = event
    events = {
        'type': event.type,
        'widget': event.widget,
        'num': event.num,
        'x': event.x, # on the widget, not on screen
        'y': event.y,
        'x_root': event.x_root, # position on the screen
        'y_root': event.y_root,
    }
    result = ''
    for key, value in events.items():
        result += f'{key}: {value}\n'
    label.config(text=result)

def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width=5)
    prev = event

root = Tk()
label = ttk.Label(root)
label.pack(side=LEFT, anchor='nw')

canvas = Canvas(root, width=640, height=480, background='white')
canvas.pack()

# 3 buttons for mouse
# 1 - left
# 2 - wheel
# 3 - right

# Event format                     | Description
# <Button>, <ButtonPress>          | User pressed any button
# <Button-1>, <ButtonPress-1>, <1> | User pressed 1 button
# <ButtonRelease-1>                | User released 1 button
# <Double-Button-1> (Triple)       | Double-click button 1
# <Enter>                          | Mouse entered widget area
# <Leave>                          | Mouse left widget area
# <Motion>                         | Mouse was moved
# <B1-Motion>                      | Mouse was was moved with B1 held down

canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)

root.mainloop()
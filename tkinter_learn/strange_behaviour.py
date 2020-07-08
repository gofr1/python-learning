#!/usr/bin/env python3

from tkinter import Tk, Canvas, HORIZONTAL, VERTICAL
from tkinter import ttk

root = Tk()

canvas = Canvas(root, scrollregion=(0,0,640,480), bg='white')
xscroll = ttk.Scrollbar(root, orient=HORIZONTAL, command=canvas.xview)
yscroll = ttk.Scrollbar(root, orient=VERTICAL, command=canvas.yview)

canvas.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

canvas.grid(row=1, column=0)
xscroll.grid(row=2, column=0, sticky='ew')
yscroll.grid(row=1, column=1, sticky='ns')

# # all ovals will be drawn in a top left corner of the canvas...
# def canvas_click(event):
#     x = event.x
#     y = event.y
#     canvas.create_oval((x-5, y-5, x+5, y+5), fill='green')

# ... to fix it we need to use canvasx/y 
def canvas_click(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    canvas.create_oval((x-5, y-5, x+5, y+5), fill='green')

canvas.bind('<1>', canvas_click)

root.mainloop()
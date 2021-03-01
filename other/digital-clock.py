from tkinter import Label, Tk 
import time

wnd = Tk() 
wnd.title("Simple Digital Clock") 
wnd.resizable(0,0)

font = ("Courier", 72, 'bold')
background_colour = "#000000"
foreground_colour = "#ffffff"
border_width = 125

label = Label(
    wnd, 
    font=font, 
    bg=background_colour, 
    fg=foreground_colour, 
    bd=border_width
) 
label.grid(row=0, column=1)

def simple_digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, simple_digital_clock)

simple_digital_clock()
wnd.mainloop()
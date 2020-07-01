#!/usr/bin/env python3

from tkinter import Tk, Label, mainloop

def main():
    root = Tk()
    Label(root, text='Hello, Tkinter!').pack()
    root.mainloop()

if __name__ == '__main__':
    main()
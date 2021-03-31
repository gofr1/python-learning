#!/usr/bin/env python3

import tkinter as tk

VERSION = '0.1'

class Snake():
    def __init__(self):
        pass

    def move(self, key):
        pass

class Application(tk.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(
            self,
            text = f'Demo'
        ).grid(row = 0, column = 0, columnspan = 2, sticky = tk.W)

def main():
    root = tk.Tk()
    root.title(f'Snake ver. {VERSION}')
    app = Application(root)
    root.mainloop()

if __name__ == '__main__':
    main()
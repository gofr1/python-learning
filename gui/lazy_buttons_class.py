from tkinter import Tk, Frame, Button

class Application(Frame):
    '''GUI app with 3 buttons'''
    def __init__(self, master):
        '''Frame initiation'''
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        '''Creates 3 useless buttons'''
        bttn1 = Button(self, text="I am doing nothing!")
        bttn1.grid()
        
        bttn2 = Button(self) 
        bttn2.grid()
        bttn2.configure(text="Me too")
        
        bttn3 = Button(self)
        bttn3.grid()
        bttn3["text"] = "And me!"

# main part
root = Tk()
root.title("Useless buttons")
root.geometry("200x95")

app = Application(root)

root.mainloop()
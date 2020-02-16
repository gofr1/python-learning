from tkinter import Tk, Frame, Button

class Application(Frame):
    '''GUI app that counts button clicks'''
    def __init__(self, master):
        '''Frame initiation'''
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()

    def create_widget(self):
        '''Creates a button which shows click count'''
        self.bttn = Button(self, command=self.update_count) # another way to set a command...
        self.bttn["text"] = "Click count: 0"
        #self.bttn["command"] = self.update_count # ... is here
        self.bttn.grid()
    
    def update_count(self):
        '''Increments counter'''
        self.bttn_clicks += 1
        self.bttn["text"] = "Click count: {}".format(self.bttn_clicks)

# main part
root = Tk()
root.title("Clicks count")
root.geometry("200x50")

app = Application(root)

root.mainloop()
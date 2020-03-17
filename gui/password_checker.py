
from tkinter import Tk, Frame, Button, Label, Entry, END, W, DISABLED

class Application(Frame):
    '''GUI app that counts button clicks'''
    def __init__(self, master):
        '''Frame initiation'''
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        '''Creates a button and text frame'''
        self.init_lbl = Label(self, text="")
        self.init_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.pw_lbl = Label(self, text="Enter the password: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)

        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)

        self.submit_bttn = Button(self, command=self.check_secret, text="Submit")
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)
        self.submit_bttn.grid()
    
    def check_secret(self):
        '''Check if secret is the same as entered password'''
        contents = self.pw_ent.get()
        if contents == 'swordfish':
            message = "Access granted"
            self.pw_ent['state'] = DISABLED # make entry field disabled after correct password entry
        else:
            message = "Incorrect password, please re-enter"
        self.pw_ent.delete(0, END)
        self.init_lbl['text'] = message

# main part
root = Tk()
root.title("Pa$$word checker")
root.geometry("300x100")

app = Application(root)

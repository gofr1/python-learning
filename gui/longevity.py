from tkinter import Tk, Frame, Button, Label, Entry, Text

class Application(Frame):
    '''GUI app that know secret of longevity'''
    def __init__(self, master):
        '''Frame initiation'''
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        """Button, text field and text label"""
        self.init_lbl = Label(self, text="To obtain secret of longevity enter the password")
        self.init_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        # row and column determine the element position
        # relative to parent object (left-top corner of the frame) 
        # --------------------------------------------
        # row=0, col=0 | row=0,  col=1 | row=0,  col=2
        # --------------------------------------------
        # row=1, col=0 | row=1,  col=1 | row=1,  col=2
        # --------------------------------------------
        # row=2, col=0 | row=2,  col=1 | row=2,  col=2
        # --------------------------------------------
        #
        # for row = 0, column = 0, columnspan = 2:
        # ------------------------------------------------
        # Text goes here                 |  row=0,  col=2
        # ------------------------------------------------
        #  row=1, col=0 | r ow=1,  col=1 |  row=1,  col=2
        # ------------------------------------------------
        # sticky is align basically
        # N - top, S - bottom, E - right, W - left (like sides of the world)
        #
        self.pw_lbl = Label(self, text="Enter the password: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
        
        # text field for password
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)

        # submit button
        self.submit_bttn = Button(self, text="Get the secret", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)
        
        # text area
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD) # wrap maybe NONR, CHAR and WORD
        self.secret_txt.grid(row = 3, column = 0, sticky = W)
        
    def reveal(self):
        '''Reply with different messages based on password entered'''
        contents = self.pw_ent.get() # get the text entry from Entry or Text object
        if contents == 'secret':
            message = "If you want to live till 100 years, you need to get to 99 " \
                "and then live very carefully"
        else:
            message = "Incorrect password, please re-enter"
        self.pw_ent.delete(0, END)
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message) # that method only insert in possition 0.0
    
# main part
root = Tk()
root.title("Longevity")
root.geometry("600x150")
app = Application(root)
root.mainloop()
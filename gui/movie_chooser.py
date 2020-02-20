from tkinter import Tk, Frame, Button, Label, Entry, Text, BooleanVar, Checkbutton, END, WORD, W

class Application(Frame):
    '''GUI app that allows to choose your favorite genres all-in-ones!'''
    def __init__(self, master):
        '''Frame initiation'''
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Elements that will help to choose"""
        # Label with description
        Label(self,
              text="Choose everything you like:",
              ).grid(row = 1, column = 0, sticky = W)
        # comedy flag
        self.likes_comedy = BooleanVar()
        Checkbutton(self,
                     text = "Comedy",
                     variable = self.likes_comedy,
                     command = self.update_text
                     ).grid(row = 2, column = 0, sticky = W)
        # drama flag
        self.likes_drama = BooleanVar()
        Checkbutton(self,
                     text = "Drama",
                     variable = self.likes_drama,
                     command = self.update_text
                     ).grid(row = 3, column = 0, sticky = W)
        # action flag
        self.likes_action = BooleanVar()
        Checkbutton(self,
                     text = "Action",
                     variable = self.likes_action,
                     command = self.update_text
                     ).grid(row = 4, column = 0, sticky = W)
        # text area with results
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)
    
    def update_text(self):
        '''refreshes text area while user changes his preferences'''
        likes = ""
        if self.likes_comedy.get():
            likes += "You like comedies.\n"
        if self.likes_drama.get():
            likes += "You like drama.\n"
        if self.likes_action.get():
            likes += "You like action.\n"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)

# main part
root = Tk()
root.title("Kinoman")
app = Application(root)
root.mainloop()
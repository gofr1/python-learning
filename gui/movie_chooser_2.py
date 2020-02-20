from tkinter import Tk, Frame, Label, Text, Radiobutton, StringVar, END, WORD, W

class Application(Frame):
    '''GUI app that allows to choose your favorite genre!'''
    def __init__(self, master):
        '''Frame initiation'''
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Elements that will help to choose"""
        # Label with description
        Label(self,
              text="Choose your favorite genre!",
              ).grid(row = 0, column = 0, sticky = W)
        
        Label(self,
              text="Choose only one: ",
              ).grid(row = 1, column = 0, sticky = W)

        # variable will store a favorite genre
        self.favorite = StringVar()
        self.favorite.set(None)
        
        # State of the switch
        Radiobutton(
            self,
            text = "Comedy",
            variable = self.favorite,
            value = "a comedy",
            command = self.update_text
        ).grid(row = 2, column = 0, sticky = W)

        Radiobutton(
            self,
            text = "Drama",
            variable = self.favorite,
            value = "a drama",
            command = self.update_text
        ).grid(row = 3, column = 0, sticky = W)

        Radiobutton(
            self,
            text = "Action",
            variable = self.favorite,
            value = "an action",
            command = self.update_text
        ).grid(row = 4, column = 0, sticky = 'W')
        
        # text area w/ results
        self.result_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.result_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        '''refreshes text area while user changes his preferences'''
        message = "Your favorite genre is "
        message += self.favorite.get()
        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, message)

# main part
root = Tk()
root.title("Kinoman 2")
root.geometry("400x200")
app = Application(root)
root.mainloop()
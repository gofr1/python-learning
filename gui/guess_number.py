from tkinter import Tk, Frame, Label, Entry, Text, Radiobutton, StringVar, END, WORD, W, BooleanVar, Checkbutton, Button
from random import randint

class GuessNumber(Frame):
    '''GUI for guess number game'''
    def __init__(self, master):
        super(GuessNumber, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        '''generates controls'''
        Label(
            self,
            text = "Enter the max number, that can be generated (5:100)"
        ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.num_ent = Entry(self)
        self.num_ent.grid(row = 1, column = 0, sticky = W)

        self.guess_bttn = Button(
            self,
            text = "Start!",
            command = self.start_game
        )
        self.guess_bttn.grid(row = 1, column = 1, sticky = W)

        self.interaction_txt = Text(self, width = 65, height = 5, wrap = WORD)
        self.interaction_txt.grid(row = 2, column = 0, columnspan = 2, sticky = W)
    
    def check_num(self):
        try:
            number = int(self.num_ent.get())
        except ValueError:
            self.print_message("It must be a number!")
        else:
            return number
    
    def print_message(self, message):
        self.interaction_txt.delete(0.0, END)
        self.interaction_txt.insert(0.0, message)

    def start_game(self):
        number = self.check_num()
        message = ''
        if number < 5:
            message = "Number is less then five, lets make it ten!"
            number = 10
        elif number > 100:
            message = "Number is greater then 100, so lets make it 100"
            number = 100

        self.number_to_guess = randint(0, number-1)
        self.number_of_guesses = (number // 4) + randint(0,4)

        self.print_message(message + "You are given {} tries. Enter the number!".format(self.number_of_guesses))
        self.guess_bttn['text'] = 'Guess!'
        self.guess_bttn['command'] = self.game
    
    def game(self):
        num = self.check_num()
        if self.number_of_guesses > 0:
            self.number_of_guesses -= 1
            if num < self.number_to_guess:
                self.print_message("Less! You have {} more tries".format(self.number_of_guesses))
            if num > self.number_to_guess:
                self.print_message("Greater! You have {} more tries".format(self.number_of_guesses))
            if num == self.number_to_guess:
                self.print_message("You win!")
                self.restart_game()
        if self.number_of_guesses == 0:
            self.print_message("You loose! The number was {}".format(self.number_to_guess))
            self.restart_game()

    def restart_game(self):
        self.guess_bttn['text'] = "Start!"
        self.guess_bttn['command'] = self.start_game

# main
root = Tk()
root.title("Numbers guessing")
app = GuessNumber(root)
root.mainloop()

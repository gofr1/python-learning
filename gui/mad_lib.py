# generates a story based on user inputs
from tkinter import Tk, Frame, Label, Entry, Text, Radiobutton, StringVar, END, WORD, W, BooleanVar, Checkbutton, Button

class Application(Frame):
    '''GUI app that generates a story based on user inputs'''
    def __init__(self, master):
        '''Frame initiation'''
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        '''generates controls'''
        # instructions label
        Label(
            self,
            text = 'Charecter creation params:'
        ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # name input
        Label(
            self,
            text = 'Name: '
        ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)
        
        # noun
        Label(self,
              text = 'Noun: '
        ).grid(row = 2, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, column = 1, sticky = W)

        # verb
        Label(
            self,
            text = 'Verb: '
        ).grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)
        
        # adjectives:
        Label(
            self,
            text = 'Adjectives: '
        ).grid(row = 4, column = 0, sticky = W)
        
        # itchy
        self.is_itchy = BooleanVar()
        Checkbutton(
            self,
            text = 'itchy',
            variable = self.is_itchy
        ).grid(row = 4, column = 1, sticky = W)

        # joyous
        self.is_joyous = BooleanVar()
        Checkbutton(
            self,
            text = 'joyous',
            variable = self.is_joyous
        ).grid(row = 4, column = 2, sticky = W)

        # electric
        self.is_electric = BooleanVar()
        Checkbutton(
            self,
            text = 'electric',
            variable = self.is_electric
        ).grid(row = 4, column = 3, sticky = W)

        # label of the bodyparts switcher
        Label(
            self,
            text = 'Body part:'
        ).grid(row = 5, column = 0, sticky = W)

        # this variable stores checked body part
        self.body_part = StringVar()
        self.body_part.set(None)

        # body parts switcher
        body_parts = ["navel", "big toe", "medulla"]
        column = 1
        for part in body_parts:
            Radiobutton(
                self,
                text = part,
                variable = self.body_part,
                value = part
            ).grid(row = 5, column = column, sticky = W)
            column += 1
        
        # submit button
        Button(
            self,
            text = "Generate story",
            command = self.tell_story
        ).grid(row = 6, column = 0, sticky = W)
        self.story_txt = Text(self, width = 75, height = 20, wrap = WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)

    def tell_story(self):
        '''put generated story into text area'''
        # get values from GUI
        person = self.person_ent.get().capitalize()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "itchy. "
        if self.is_joyous.get():
            adjectives += "joyous. "
        if self.is_electric.get():
            adjectives += "electric. "
        body_part = self.body_part.get()

        # story generating
        story = "Once upon a time in some lands of magic there lived {}. \
In the same time crude {} ruled the land. \
And one day {} and {} meet each other. \
Both sides feeled {} at the same time. \
The battle starts! {} finally beats off {} of {}. \
The {} wins! There is once again a peace in lands of magic! \
After that {}".format(person, noun.title(), noun, person, adjectives, person, body_part, noun, person, verb)
        
        # output
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

# main
root = Tk()
root.title("Mad Librarian")
app = Application(root)
root.mainloop()
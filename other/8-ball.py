#!/usr/bin/env python3
#! Magic 8 Ball
# is a special toy used for fortune telling process 
# or seeking guidance manufactured by Mattel and enhanced in the 1950s. 

from random import randint

all_answers = [
    # Positive Answers
    [
        'It is certain',
        'Without a doubt',
        'You may rely on it',
        'Yes definitely',
        'It is decidedly so',
        'As I see it, yes',
        'Most likely',
        'Yes',
        'Outlook good',
        'Signs point to yes'
    ],
    
    # Neutral Answers
    [
        'Reply hazy try again',
        'Better not tell you now',
        'Ask again later',
        'Cannot predict now',
        'Concentrate and ask again'
    ],
    
    # Negative Answers
    [
        'Don’t count on it',
        'Outlook not so good',
        'My sources say no',
        'Very doubtful',
        'My reply is no',
    ],
]

go_on = True

while go_on is True:
    question = input('Ask the Magic 8 ball a question: (press enter to quit): ')
    
    if question == '':
        go_on = False
        print('Bye!')
    else:
        answer_type = randint(0,2)
        answers = all_answers[answer_type]
        answer_number = randint(0,len(answers))
        print(all_answers[answer_type][answer_number]) #FF2D00

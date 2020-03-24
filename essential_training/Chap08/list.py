#!/usr/bin/env python3

def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'] # list is mutable
    i = game.index('Paper')
    game.append('Computer') # add element to the end
    game.insert(3, 'Laptop') # add element in some position
    game.remove('Paper') # remove element by name
    game.pop(2) # removes element by index
    del game[1:5:2] # removes element by index, or with slicing
    game.pop() # removes last element in the list
    print(', '.join(game))
    print(game[1:5:2], i, game)
    print_list(game)

def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()

if __name__ == "__main__":
    main()
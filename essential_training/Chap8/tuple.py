#!/usr/bin/env python3

def main():
    game = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock') # tuple is immutable
    print(', '.join(game))
    print_list(game)

def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()

if __name__ == "__main__":
    main()
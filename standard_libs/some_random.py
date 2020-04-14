#!/usr/bin/env python3

import random

def main():
    # Random numbers
    print(random.random())
    
    # Coin toss
    decider = random.randrange(2) # is excluive
    if decider == 0:
        print("HEADS")
    else:
        print("TAILS")
    
    # Dice roll
    print(f"You rolled a {random.randrange(1,7)}")

    # Random choices
    lotteryWinners = random.sample(range(100), 5) # select 5 numbers from given range
    print(lotteryWinners)

    possiblePets = ["cat", "dog", "fish"]
    print(random.choice(possiblePets))
    
    # Cards shuffle
    cardsWithPictures = ["J", "Q", "K"]
    cardsWithNumbers = list(range(1,11))
    cardsSuit = ["♦", "♣", "♥", "♠"]
    
    cards = list()
    for card in cardsWithPictures:
        for suit in cardsSuit:
            cards.append(card+suit)

    for card in cardsWithNumbers:
        for suit in cardsSuit:
            cards.append(str(card)+suit)
    
    random.shuffle(cards)

    print(cards)

if __name__ == '__main__':
    main()
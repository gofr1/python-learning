from random import randint

def roll_the_dice(dice_type):
    dice_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 30, 32, 34, 48, 50, 60, 100, 120, 144]
    min_value = 1
    if dice_type in dice_types:
        return randint(min_value, dice_type)
    return 0

print(roll_the_dice(10))
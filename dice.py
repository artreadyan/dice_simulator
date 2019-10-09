import random


def roll_dice():
    roll_dice = input("Roll dice? (y/n) ")
    if roll_dice == "y":
        print(random.randint(1,6))
    else:
        exit()
    
        
while True:
    roll_dice()

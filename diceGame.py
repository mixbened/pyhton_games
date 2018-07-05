import random


# Dice Game
def dice_game(): 
    keep_going = 'Y'
    while keep_going == 'Y':
        for x in range(10):
            random_num = random.randint(1,6)
        print(random_num)
        keep_going = input('Roll Again? (Y/N)')

print('Hey Guys, this is the Dice Game!')
dice_game()
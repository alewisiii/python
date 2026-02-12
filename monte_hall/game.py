""" This code is for playing the game onthe command prompt
"""
import random

from monte_game import MonteGame

NUM_DOORS = 3
def get_number(message):
    """ Get a valid number from the user.
    """

    while True:
        user_input = input(message)
        try:
            number = int(user_input)
            if 1 <= number <= NUM_DOORS:
                return number
            print("Number out of range")
        except ValueError:
            print("The value must be a number")

def pick_another_door(user_choice,wrong_choice):
    """ Based on the choice and wrong answer, pick a different door """

    while True:
        door = random.randint(1, 3)
        if door not in (user_choice,wrong_choice):
            return door

game = MonteGame(NUM_DOORS)
choice = get_number(f"pick a door between 1 and {NUM_DOORS}.  ")
print(f"You picked {choice}")
wrong = game.wrong_door(choice)
print(f"Door {wrong} is the wrong door")
change = input("Do you want to change your answer[y/n]")
if change == 'y':
    choice = pick_another_door(choice,wrong)
    print (f"the new door is {choice}\n")


answer = game.correct_answer()
if answer == choice:
    print(f"{choice} is correct")
else:
    print(f"You are incorrect the answer was {answer}.")

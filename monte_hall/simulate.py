""" Simulates playing the game many times and returns the number
    of successes 
"""

import random
from monte_game import MonteGame

DOORS = 3
TOTAL_GAMES = 100000

def pick_another_door(choice,wrong):
    """ Pick another door after being given the wrong choice """

    while True:
        door = random.randint(1, 3)
        if door not in (choice,wrong):
            return door

def simulate(make_change):
    """ Simulate playing the game based on either keeping the answer or
        changing the answer.  
    """
    correct = 0
    for _ in range(TOTAL_GAMES):
        game = MonteGame(DOORS)
        choice = random.randint(1, DOORS)
        if make_change is True:
            wrong = game.wrong_door(choice)
            choice = pick_another_door(choice,wrong)
        answer = game.correct_answer()
        if answer == choice:
            correct +=1
    percentage = 100* (correct / TOTAL_GAMES)
    print(f"{correct} correct out of {TOTAL_GAMES}  {percentage:.2f}%")

print ("Do not make a change")
simulate(False)
print("")
print("Change answer")
simulate(True)

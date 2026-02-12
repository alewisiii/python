""" Class to manage the doors """

import random

class MonteGame:
    """ the class tha maintains the doors
    """

    def __init__(self,no_of_doors):
        """ Set up the game  and pick a door """
        self.no_of_doors = no_of_doors
        self.door = self.pick_a_door()

    def pick_a_door(self):
        """ Pick a door to be the answer """
        return random.randint(1, self.no_of_doors)

    def new_game(self):
        """ Start a new game without making a new variable.  """
        self.door = self.pick_a_door()

    def wrong_door(self,choice):
        """ Return the wrong door; the door that is not what they choose and not
        the correct answer
        """
        while True:
            door = self.pick_a_door()
            if door not in (choice,self.door):
                return door

    def correct_answer(self):
        """ Return the correct answer """
        return self.door

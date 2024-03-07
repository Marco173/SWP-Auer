from random import random, randint

from Spieler import Player


class Computer(Player):

    def __init__(self,name="Computer" ):
        super().__init__(name)

    def option(self):
        return randint(1, 5)
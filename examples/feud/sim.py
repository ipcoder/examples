from abcEconomics import Agent, Household

class Peasant(Agent, Household):
    def init(self):
        self.kids=0
        self.food = 0

from inu.flex import    Algorithm
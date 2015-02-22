""" Autheur Giuseppe Federico 
"""

from game.agents import Agent
from game.agents.AgentAction import AgentAction

class ScoreAddAgent():
    """ Un premier agent de test
    """

    def __init__(self):
        super()
        self.cards = []
        self.answer = False


    def getAction(self, agent_state, game_state):
        inputt = input("increment score?")
        self.answer = (input == "yes")
        action = AgentAction(True)
        return action
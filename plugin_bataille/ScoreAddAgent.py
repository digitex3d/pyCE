""" Autheur Giuseppe Federico 
"""

from game.agents import Player
from game.agents.AgentAction import AgentAction

class ScoreAddAgent(Player):
    """ Un premier agent de test
    """

    def getAction(self, agent_state, game_state,event=None):
        print(event.clicked)
        action = AgentAction(True)
        return action
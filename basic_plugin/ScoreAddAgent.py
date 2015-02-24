""" Autheur Giuseppe Federico 
"""

from game.agents import Agent
from game.agents.AgentAction import AgentAction

class ScoreAddAgent(Agent):
    """ Un premier agent de test
    """

    def getAction(self, agent_state, game_state):
        action = AgentAction(True)
        return action
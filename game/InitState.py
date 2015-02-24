""" Autheur Giuseppe Federico 
"""

from game.agents import AgentState

class InitState:
    """ Cette classe représente un InitState 
    """

    def __init__(self):
        self.nb_agents = 0
        self.agentsStates = []
        self.turn = 0

    def addAgentState(self, agent_state):
        """ Ajoute un joueur au jeu
        """
        self.agentsStates.append( agent_state)
        self.nb_agents += 1
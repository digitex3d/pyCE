""" Autheur Giuseppe Federico 
"""
from game.InitState import InitState
from game.PublicGameState import PublicGameState


class Plugin:
    """ Cette classe représente un Plugin 
    """


    def __init__(self):
        test = True
        self.TABLE_PID = -1
        self.PLAYER_PID = 0
        self.opponents = []
        # Initialisation du jeu
        self.initState = InitState()

    def nextState(self, gameState, agent_action):
        """ Classe abstraite à implémenter dans le plugin.
        :return:
        """
        return None

    def GNextState(self, gameState, agent_action):
        new_state = gameState.copy()
        publicNewState = PublicGameState(new_state)
        return self.nextState(new_state, agent_action)



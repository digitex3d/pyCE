""" Autheur Giuseppe Federico 
"""
from game.InitState import InitState


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



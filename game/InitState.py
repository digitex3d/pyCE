""" Autheur Giuseppe Federico 
"""
from environment.Table import Table

from game.agents import PlayerState

class InitState:
    """ Cette classe va servir pour initialiser le jeu
    """

    def __init__(self):
        self.turn = 0
        self.table = Table()
        self.win = False

    def addPlayerState(self, player_state):
        """ Ajoute un joueur au jeu
        """
        self.table.addPlayer(player_state)
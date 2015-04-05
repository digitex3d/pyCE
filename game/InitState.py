""" Autheur Giuseppe Federico 
"""
from environment.DeckGenerator import DeckGenerator
from environment.CardStack import CardStack
from environment.Table import Table

from game.agents import PlayerState

class InitState:
    """ Cette classe va servir pour initialiser le jeu
    """

    def __init__(self):
        self.turn = 0
        self.table = Table()
        self.win = False

    def addPlayerState(self, hand=CardStack(), deck=CardStack()):
        """ Ajoute un joueur au jeu
        :param hand: CardStack() la main initiale
        :param deck: CardStack() le jeu initial
        :return:
        """

        self.table.addPlayer( hand, deck)

    def generateShuffledDeck(self):
        """ Générer un jeu de cartes mélangé.

        :return: (CardStack)
        """

        deck = DeckGenerator.deckFactory()
        deck.shuffle()
        return deck
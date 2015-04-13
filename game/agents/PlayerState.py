""" Autheur Giuseppe Federico 
"""

from environment.CardStack import CardStack

class PlayerState:

    def __init__(self, id=0, hand=CardStack(), deck=CardStack(),score=0,):
        """ L'état d'un joueur, sa main, son score, etc...
        :param id: l'identifiant unique du joueur
        :param hand: la main du joueur
        :param deck: le jeu de cartes
        :param score: le score
        :return:
        """

        self.id = id
        self.score = 0
        self.hand = hand
        self.deck = deck
        self.dealer = False

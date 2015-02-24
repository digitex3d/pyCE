""" Autheur Giuseppe Federico 
"""

from environment.CardStack import CardStack

class AgentState:
    """ Cette classe représente un Etat de l'agent
    """

    def __init__(self, id=0, hand=CardStack(), deck=CardStack(),score=0,):
        self.id = id
        self.score = 0
        self.hand = hand
        self.deck = deck

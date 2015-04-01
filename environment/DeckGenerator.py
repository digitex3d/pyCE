""" Autheur Giuseppe Federico 
"""
from environment.Card import Card
from environment.CardStack import CardStack


class DeckGenerator:
    """ Cette classe représente un générateur de jeu de cartes
    """

    def deckFactory():
        deck = CardStack()
        for kind in ["c","d","h","s"]:
            for value in range(1, 14):
                if(kind == "h" or kind=="d"):
                    deck.append(Card(value, "red", kind))
                else:
                    deck.append(Card(value, "black", kind))

        return deck


    deckFactory = staticmethod(deckFactory)

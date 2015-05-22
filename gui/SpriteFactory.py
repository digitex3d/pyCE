# -*- coding: utf-8 -*-
from gui.Sprites.CardSprite import CardSprite

IMG_FORMAT="gif"
DATA_PATH="data"

CARDS={
    11:"j",
    12:"q",
    13:"k"
    }

class SpriteFactory():
    def card_factory(card, x=0, y=0):
        """Factory pour les cartes; Génération d'un CardSprite à partir d'un Card.

        :param card (Card): La carte en question.
        :param x (int): Coordonné x du coin bas-gauche de la nouvelle carte.
        :param y (int): Coordonné y du coin bas-gauche de la nouvelle carte.
        :return:
        """
        if( not card.hidden ):
            if(card.value <= 10):
                file_name = str(card.value) + str(card.kind) + "." + IMG_FORMAT
            else:
                file_name = CARDS[card.value] + str(card.kind) + "." + IMG_FORMAT
        else:
             file_name ="b.gif"

        img = DATA_PATH+"/cards/"+file_name

        return CardSprite(card,img, x, y)

    card_factory = staticmethod(card_factory)

    def deck_factory(cards):
        """ Renvoie une liste de CardSprite
        """
        cardSprites = []
        for card in cards:
            cardSprites.append(SpriteFactory.card_factory(card))
        return cardSprites

    deck_factory = staticmethod(deck_factory)





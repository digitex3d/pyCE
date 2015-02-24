""" Cette classe représente une main affichable"""

from gui.CardSprite import CardSprite
from environment import CardStack
from pyglet.sprite import Sprite
import pyglet.image
import basic_plugin

DISTANCE_CARTES = 70


class CardStackDrawable():
    """ Une représentation graphique des cartes ( main )
    """

    def __init__(self, cardsSprites,proprietary ,x=0, y=0, dir="h", batch=None):
        self.x = x
        self.y = y
        self.dir = dir
        self.batch = batch
        self.proprietary = proprietary
        self.cardSprites = cardsSprites
        self.set_up()

    def update(self, cards):
        self.cardSprites = basic_plugin.SpriteFactory.deck_factory(cards)

    def set_up(self):
        """ Toujours appeler cette fonction avant d'afficher la main
        """
        if( self.dir == "v" ):
            # Affichage vertical
            dy=0
            for card in self.cardSprites:
                card.rotation = 90.0
                card.x = self.x
                card.y = self.y + dy
                dy = dy + DISTANCE_CARTES
        if( self.dir == "h" ):
            # Affichage horizontal
            dx=0
            for card in self.cardSprites:

                card.x = self.x + dx
                card.y = self.y
                dx = dx + DISTANCE_CARTES
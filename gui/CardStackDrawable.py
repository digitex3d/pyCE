""" Cette classe représente une main affichable"""

from gui.SpriteFactory import SpriteFactory
from gui.CardSprite import CardSprite
from environment import CardStack
from pyglet.sprite import Sprite
import pyglet.image


DISTANCE_CARTES = 70
IMG_FORMAT="gif"
DATA_PATH="data"

class CardStackDrawable():
    """ Une représentation graphique des cartes ( main )
    """

    def __init__(self, cardsSprites=[],proprietary=0 ,x=0, y=0, dir="h", batch=None):
        self.x = x
        self.y = y
        self.dir = dir
        self.batch = batch
        self.proprietary = proprietary
        self.cardSprites = cardsSprites
        self.width = None
        self.height = None
        self.set_up()



    def update(self, cards):
        """ On met à jour la main avec les nouveaux cartes
        """

        self.cardSprites = SpriteFactory.deck_factory(cards)
        self.set_up()

    def set_up(self):
        """ Toujours appeler cette fonction avant d'afficher la main modifié
        """
        theight = 0
        twidth = 0
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
                twidth += card.width
                theight = card.height
            self.width = twidth
            self.height = theight

    def isClicked(self, x,y):
        return x > self.x and \
               x < self.x+ self.width and \
               y > self.y and \
               y < self.y + self.height

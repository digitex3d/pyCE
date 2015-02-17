""" Cette classe représente une main affichable"""

from gui.CardSprite import CardSprite
from environment import CardStack
from pyglet.sprite import Sprite
import pyglet.image

DISTANCE_CARTES = 70


class CardStackDrawable(list):
    """ Une représentation graphique des cartes ( main )
    """

    def __init__(self,x=0, y=0, dir="h", batch=None,):
        self.x = x
        self.y = y
        self.dir = dir
        self.batch = batch


    def set_up(self):
        """ Toujours appeler cette fonction avant d'afficher la main
        """
        if( self.dir == "v" ):
            # Affichage vertical
            dy=0
            for card in self:
                card.rotation = 90.0
                card.x = self.x
                card.y = self.y + dy
                dy = dy + DISTANCE_CARTES
        if( self.dir == "h" ):
            # Affichage horizontal
            dx=0
            for card in self:

                card.x = self.x + dx
                card.y = self.y
                dx = dx + DISTANCE_CARTES
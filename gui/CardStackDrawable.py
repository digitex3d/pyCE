""" Cette classe représente un jeu de carte affichable"""

from gui.CardSprite import CardSprite
from environment import CardStack
from pyglet.sprite import Sprite
import pyglet.image

""" Une représentation graphique des cartes """
class CardStackDrawable():
    def __init__(self, drawableCards,batch, x=0, y=0, dir="h"):
        self.drawableCards = drawableCards
        self.x = x
        self.y = y
        self.dir = dir
        self.batch = batch

    def set_up(self):
        if( self.dir == "v" ):
            dy=0
            for card in self.drawableCards:
                card.x = self.x
                card.y = self.y + dy
                dy = dy + 100
        if( self.dir == "h" ):
            dx=0
            for card in self.drawableCards:
                card.x = self.x + dx
                card.y = self.y
                dx = dx + 100
                

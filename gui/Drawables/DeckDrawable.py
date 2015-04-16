""" Autheur Giuseppe Federico 
"""
import pyglet
from gui.Default import DATA_PATH
from gui.Drawables.Drawable import Drawable
from gui.Sprites.ClickableSprite import ClickableSprite
import logging

class DeckDrawable(Drawable):
    """ Cette classe représente une pile de cartes affichable.
    """

    def __init__(self, x, y, pid, dir="h"):
        """ Initialise une pile de cartes affichable.

        :param x (int): Coin bas-gauche x.
        :param y (int): Coin bas-gauche y.
        :param dir: La direction de la pile.
        :param pid: L'id du joeur propriétaire de la pile.
        :return:
        """

        Drawable.__init__(self,x,y)
        self.pid = pid
        self.dir = dir
        self.visible = False
        self.name = "Deck"
        # Image de la pile des cartes
        deck_image = pyglet.image.load(DATA_PATH + "cards/deck"+dir+".gif")
        self.sprites.append(ClickableSprite(deck_image,x,y))

    def update(self, gameState):
        if( self.pid != -1):
            if( len(gameState.table.players[self.pid].deck) == 0):
                self.visible = False
        else:
            if( len(gameState.table.deck) == 0):
                self.visible = False



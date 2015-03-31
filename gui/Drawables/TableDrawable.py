""" Autheur Giuseppe Federico 
"""

from gui.SpriteFactory import SpriteFactory
from gui.Drawables import CardStackDrawable
from gui.Drawables.Drawable import Drawable
from gui.Sprites.ClickableSprite import ClickableSprite
import pyglet
import logging

DISTANCE_CARTES = 100

DATA_PATH = "data/"

class TableDrawable(Drawable):
    """ Cette classe représente une TableDrawable, l'endroit où les cartes seront déposé
    """

    def __init__(self, x,y,h,w):
        Drawable.__init__(self, x,y,h,w)
        self.height = h
        self.width = w


        self.pid = -1

          # Fond vert
        table_image = pyglet.image.load(DATA_PATH + "table/green.jpg")
        self.table_sprite = ClickableSprite(table_image,x,y)
        self.sprites.append(self.table_sprite)




    def update(self, gameState):
        """ On met à jour la table
        """
        cards = gameState.table.table
        self.sprites = []
        self.sprites.append(self.table_sprite)
        self.sprites.extend(SpriteFactory.deck_factory(cards))

        # Affichage horizontal
        dx=0
        for cardSprite in self.sprites:
            cardSprite.x = self.x + dx
            cardSprite.y = self.y
            dx = dx + DISTANCE_CARTES


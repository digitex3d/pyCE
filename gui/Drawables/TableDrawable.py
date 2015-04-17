""" Autheur Giuseppe Federico 
"""

from gui.SpriteFactory import SpriteFactory
from gui.Drawables import CardStackDrawable
from gui.Drawables.Drawable import Drawable
from gui.Sprites.ClickableSprite import ClickableSprite
import pyglet
import logging

DISTANCE_CARTES_X = 100
DISTANCE_CARTES_Y = 150

DATA_PATH = "data/"

class TableDrawable(Drawable):
    """ Cette classe représente une TableDrawable, l'endroit où les cartes seront déposé
    """

    def __init__(self, x,y,h,w):
        Drawable.__init__(self, x,y,h,w)
        self.height = h
        self.width = w
        self.name = "Table"


        self.pid = -1

        # Fond vert
        table_image = pyglet.image.load(DATA_PATH + "table/green.png")
        self.table_sprite = ClickableSprite(table_image,x,y)
        self.sprites.append(self.table_sprite)




    def update(self, gameState):
        """ On met à jour la table
        """

        cards = gameState.table.table
        self.sprites = []
        self.sprites.append(self.table_sprite)
        self.sprites.extend(SpriteFactory.deck_factory(cards))

        # Les cartes sont ordonnées par rapport à l'ordre de tirage.
        if(gameState.drawingStyle == 1):
            nb_c = len(self.sprites)
            distance_x = DISTANCE_CARTES_X * 1/(nb_c/12)
            distance_y = DISTANCE_CARTES_Y * 1

            # Affichage horizontal
            dx=0
            dy=0
            origin_x = self.x + 30
            origin_y = self.y + 380
            for sprite in self.sprites:
                if (sprite == self.table_sprite):
                    sprite.x =  self.x
                    sprite.y = self.y
                else:
                    if( origin_x+dx > origin_x + 400):
                        dx = 0
                        dy -= distance_y
                    sprite.x = origin_x + dx
                    sprite.y = origin_y + dy
                    dx = dx + distance_x

         # Les cartes sont ordonnées en face de leur propriétaire
        if (gameState.drawingStyle == 0):
            pos = []
            pos.append((480,210))
            pos.append((270, 370))
            pos.append((480, 520))
            pos.append((700, 370))

            i=0
            for sprite in self.sprites:
                if (sprite == self.table_sprite):
                    sprite.x =  self.x
                    sprite.y = self.y
                else:
                    if(len(cards) > 0 ):
                        card = cards[i]
                        if(card.owner == -1):
                            sprite.x = 480
                            sprite.y = 370
                        else:
                            sprite.x = pos[card.owner][0]
                            sprite.y = pos[card.owner][1]
                    i+=1



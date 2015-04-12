""" Cette classe représente une main affichable"""
from gui.Drawables.Drawable import Drawable
from gui.Drawables.Utils import Utils

from gui.SpriteFactory import SpriteFactory
from gui.Sprites.ClickableSprite import ClickableSprite


DISTANCE_CARTES = 70
IMG_FORMAT="gif"
DATA_PATH="data/"
import pyglet

class CardStackDrawable(Drawable):
    """ Une représentation graphique des cartes ( main )
    """

    def __init__(self, x, y, pid, dir="h"):
        """
        :param x:
        :param y:
        :param dir: La direction des cartes à l'affichage
        :param pid: le player id
        :return:
        """
        Drawable.__init__(self,x,y)
        self.pid = pid
        self.dir = dir
        self.name = "CardStack"
         # Fond gris
        space_image = pyglet.image.load(DATA_PATH + "table/playerSpace"+dir+".png")
        self.space_sprite = ClickableSprite(space_image,x,y)

    def getPid(self):
        return self.pid

    def update(self, gameState):
        """ On met à jour la main avec les nouveaux cartes
        """

        cards = gameState.table.players[self.pid].hand

        self.sprites = []
        self.sprites.append(self.space_sprite)
        self.sprites.extend(SpriteFactory.deck_factory(cards))


        if( self.dir == "v" ):
            # Affichage vertical
            nb_c = len(self.sprites)
            distance_y = DISTANCE_CARTES * 1/(nb_c/5)

            dy = 0
            for sprite in self.sprites:
                if( sprite == self.space_sprite):
                    sprite.x = self.x
                    sprite.y = self.y
                else:
                    sprite.rotate(90)
                    sprite.x = self.x
                    sprite.y = self.y + dy
                    dy = dy + distance_y





        if( self.dir == "h" ):
            # Affichage horizontal
            nb_c = len(self.sprites)
            distance_x = DISTANCE_CARTES * 1/(nb_c/5)

            dx = 0


            for sprite in self.sprites:
                if( sprite == self.space_sprite):
                    sprite.x = self.x
                    sprite.y = self.y
                else:
                    sprite.x = self.x + dx
                    sprite.y = self.y
                    dx = dx + distance_x
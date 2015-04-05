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

        #TODO: resoudre probleme rotation
        theight = 0
        twidth = 0
        if( self.dir == "v" ):
            # Affichage vertical
            dy=0
            for cardSprite in self.sprites:
                # set it so it will rotate around the center
                #cardSprite.image.anchor_x = cardSprite.image.width / 2
                #cardSprite.image.anchor_y = cardSprite.image.height / 2
                cardSprite.rotation = 90.0
                cardSprite.x = self.x
                cardSprite.y = self.y + dy
                dy = dy - DISTANCE_CARTES
                twidth = cardSprite.width
                theight = dy
            self.width = twidth
            self.height = theight
            print(self.x)
            print(self.y)
            print(self.height)
            print(self.width)


        if( self.dir == "h" ):
            # Affichage horizontal
            dx=0

            for cardSprite in self.sprites:
                cardSprite.x = self.x + dx
                cardSprite.y = self.y
                dx = dx + DISTANCE_CARTES
                twidth = dx
                theight = cardSprite.height
            self.width = twidth
            self.height = theight + cardSprite.height
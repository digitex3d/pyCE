

from environment import Card
from pyglet.sprite import Sprite
import pyglet.image
from gui.Sprites.ClickableSprite import ClickableSprite

BACK_SIDE_IMAGE = pyglet.image.load("data/cards/b.gif")

class CardSprite(ClickableSprite):
    """ Cette classe représente le Sprite d'une carte"""

    def __init__(self, card, img, x=0, y=0, blend_src=770, blend_dest=771, batch=None, group=None, usage='dynamic'):
        img = pyglet.image.load(img)
        super(CardSprite, self).__init__(img, x, y, blend_src,blend_dest, batch, group, usage)
        self.card=card
        self.side=1
        self.card_image = img


    def switch_side(self):
        """ Permet de changer le coté affiché d'une carte
        """
        if( self.side == 1 ):
            self.side = 0
            self.image =  BACK_SIDE_IMAGE
        else:
            self.side = 1
            self.image = self.card_image




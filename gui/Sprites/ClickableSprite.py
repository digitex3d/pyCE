""" Autheur Giuseppe Federico 
"""

import pyglet
from pyglet.sprite import Sprite

class ClickableSprite(Sprite):
    """ Cette classe est un Sprite qui peut être cliqué
    """

    def __init__(self, *args, **kwargs):
        Sprite.__init__(self, *args, **kwargs)

    def rotate(self, degree):
        self.rotation = degree

    def isClicked(self, x,y):
        """Renvoi True si le sprite a reçu un click; False sinon.

        :param x: coord x du click.
        :param y: coord y du click.
        :return:
        """
        return x > self.x and \
               x < self.x+ self.width and \
               y > self.y and \
               y < self.y + self.height


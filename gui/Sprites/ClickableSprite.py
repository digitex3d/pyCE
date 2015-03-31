""" Autheur Giuseppe Federico 
"""

import pyglet
from pyglet.sprite import Sprite

class ClickableSprite(Sprite):
    """ Cette classe est un Sprite qui peut être cliqué
    """

    def __init__(self, *args, **kwargs):
        Sprite.__init__(self, *args, **kwargs)

    def isClicked(self, x,y):
        return x > self.x and \
               x < self.x+ self.width and \
               y > self.y and \
               y < self.y + self.height


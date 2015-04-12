""" Autheur Giuseppe Federico 
"""
import abc
import pyglet




class Drawable:
    """ Cette classe représente un Drawable 
    """

    def __init__(self, x, y,h=0,w=0, name=None):
        self.sprites = []
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        self.visible = True
        self.name = name


    def bordersVisible(self, value):
        self.showBorders = value

    def isClicked(self,x,y):
        """
        Renvoi vrai si un de ses sprites a été clicqué
        :return:
        """

        resu = False
        if( self.visible):
            for sprite in self.sprites:
                if("isClicked" in dir(sprite) ):
                    resu = resu or  sprite.isClicked(x,y)


        return resu

    def getSprites(self):
        if(self.visible):
            return self.sprites
        else:
            return  []

    @abc.abstractmethod
    def update(self, gameState):
        """ Mettre à jour le drawable au changement du gamestate
        """





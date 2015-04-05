""" Autheur Giuseppe Federico 
"""
import abc
import pyglet




class Drawable:
    """ Cette classe représente un Drawable 
    """

    def __init__(self, x, y,h=0,w=0, showBorders=False):
        self.sprites = []
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        self.showBorders = showBorders
        self.visible = True


    def bordersVisible(self, value):
        self.showBorders = value

    def isClicked(self,x,y):
        """
        Renvoi vrai si un de ses sprites a été clicqué
        :return:
        """

        resu = False
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

    def drawableBorders(self):
        """ Cette fonction renvoie les points de la zone qui peut recevoir un click.
        """



        bl = (self.x, self.y)
        br = (self.x + self.width, self.y)
        tl = (self.x, self.y + self.height)
        tr = (self.x + self.width , self.y+self.height)


        vl = [bl[0], bl[1],
                br[0], br[1],
                tl[0], tl[1],
                tr[0], tr[1]]

        return vl



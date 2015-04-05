""" Autheur Giuseppe Federico 
"""
from pyglet.text import Label
from pyglet.sprite import Sprite
import pyglet
from gui.Components.Component import Component
from gui.Drawables.Drawable import Drawable


DATA_PATH = "data/"

class HUDComponent(Component):
    """ Cette classe représente un HUD 
    """

    def __init__(self, window):
        Component.__init__(self, window)


        # Fond vert
        self.background = pyglet.image.load(DATA_PATH + "table/table.jpg")
        back_drawable = Drawable(0,0)
        back_drawable.sprites.append(Sprite(self.background,0,0))
        self.drawables.append(back_drawable)

        # On ajoute le score au hud
        self.drawables.append(ScoreLabel(100,100,0))
        self.drawables.append(ScoreLabel(100,500 ,1))

        # On ajoute le label win
        self.drawables.append(WinLabel(100,200))



class ScoreLabel(Drawable):
    """ Cette classe représente une partie du HUD où le score du joueur sera
        éventuelment affiché.
    """

    #TODO: bien positioner le ScoreLabel par rapport à la résolution de l'écran
    def __init__(self, x , y, pid ):
        Drawable.__init__(self, x , y)
        self.label = Label('0',
                          font_name='Times New Roman',
                          font_size=36,
                          x=x, y=y)

        #TODO: c'est pas la bonne taille
        self.height = 20
        self.width =20
        self.pid = pid
        self.sprites.append(self.label)

    def update(self, gameState):
        self.label.text = str(gameState.table.players[self.pid].score)

class WinLabel(Drawable):
    """ Cette classe représente une partie du HUD où le score du joueur sera
        éventuelment affiché.
    """

    #TODO: bien positioner le ScoreLabel par rapport à la résolution de l'écran
    def __init__(self, x , y):
        Drawable.__init__(self, x , y)
        self.label = Label('',
                          font_name='Times New Roman',
                          font_size=42,
                          x=x, y=y)

        #TODO: c'est pas la bonne taille
        self.height = 20
        self.width =20
        self.sprites.append(self.label)

    def update(self, gameState):
        if( gameState.win):
            self.label.text = "WIN!!"
        if( gameState.lose):
            self.label.text = "LOST!!"
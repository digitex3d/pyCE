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
        # On initialise un ScoreLabel avec la valeur de l'état de jeu initial et la fenetre
        self.score_label = ScoreLabel(20 , 20)

        # Fond vert
        self.background = pyglet.image.load(DATA_PATH + "table/table.jpg")
        back_drawable = Drawable(0,0)
        back_drawable.sprites.append(Sprite(self.background,0,0))
        self.drawables.append(back_drawable)

        # On ajoute le score au hud
        self.drawables.append(ScoreLabel(100,100))



class ScoreLabel(Drawable):
    """ Cette classe représente une partie du HUD où le score du joueur sera
        éventuelment affiché.
    """

    #TODO: bien positioner le ScoreLabel par rapport à la résolution de l'écran
    def __init__(self, x , y ):
        Drawable.__init__(self, x , y)
        label = Label('0',
                          font_name='Times New Roman',
                          font_size=36,
                          x=x, y=y)

        #TODO: c'est pas la bonne taille
        self.height = 20
        self.width =20

        self.sprites.append(label)

    def update(self, gameState):
        self.text = "0"

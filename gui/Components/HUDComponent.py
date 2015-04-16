""" Autheur Giuseppe Federico 
"""
from pyglet.text import Label
from pyglet.sprite import Sprite
import pyglet
from gui.Components.Component import Component
from gui.Drawables.Drawable import Drawable
from gui.Sprites.ClickableSprite import ClickableSprite


DATA_PATH = "data/"

class HUDComponent(Component):
    """ Cette classe représente un HUD 
    """

    def __init__(self, window):
        Component.__init__(self, window)
        self.window = window

        # On ajoute le score au hud
        self.drawables.append(ScoreLabel(780,730,0))
        self.drawables.append(ScoreLabel(780,700 ,1))

        # On ajoute le label win
        self.drawables.append(WinLabel(100,200))

        # On ajoute le dialog
        self.drawables.append(DialogDrawable(330, 20))


        # On ajoute le dialog
        self.drawables.append(GameInfo(700, 80))





class ScoreLabel(Drawable):
    """ Cette classe représente une partie du HUD où le score du joueur sera
        éventuelment affiché.
    """

    def __init__(self, x , y, pid ):
        Drawable.__init__(self, x , y)
        self.label = Label('0',
                          font_name='Times New Roman',
                          font_size=26,
                          x=x, y=y)

        self.pid = pid
        self.sprites.append(self.label)

    def update(self, gameState):
        self.label.text ="Player " + str(self.pid) +":" + \
                         str(gameState.table.players[self.pid].score)

class GameInfo(Drawable):
    """ Cette classe représente une partie du HUD où le score du joueur sera
        éventuelment affiché.
    """

    def __init__(self, x , y ):
        Drawable.__init__(self, x , y)

    def update(self, gameState):
        dy = 0
        if( self.y - (dy+50) < 0):
            self.sprites.remove(0)
            dy += 22
        for msg in gameState.infoLog:
            self.sprites.append(Label(msg,
                          font_name='Times New Roman',
                          font_size=18,
                          x=self.x,y=self.y+dy))
            dy -= 22

class WinLabel(Drawable):
    """ Le label Win/Lose
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

class DialogDrawable(Drawable):
    """ Le bouton Start/End game.
    """

    def __init__(self, x, y):
        Drawable.__init__(self,x,y)
        self.name = "Dialog"


        dialogImage = pyglet.image.load(DATA_PATH + "HUD/dialog.png")
        self.sprites.append(ClickableSprite(dialogImage,x,y))

        self.labelTitle = Label('PyCE',
                          font_name='Times New Roman',
                          font_size=38,
                          x=x+(dialogImage.width)/3 ,
                          y=y+(dialogImage.height) - 48)
        self.sprites.append(self.labelTitle)

        self.labelMsg = Label('Start a new game',
                          font_name='Times New Roman',
                          font_size=28,
                          x=x+10, y=y+(dialogImage.height)-100)
        self.sprites.append(self.labelMsg)

        self.labelButton = Label('Start',
                          font_name='Times New Roman',
                          font_size=28,
                          x=x+(dialogImage.width)/3, y=y+45)
        self.sprites.append(self.labelButton)




    def update(self, gameState):
        self.visible = gameState.dialog.visible
        self.labelTitle.text = gameState.dialog.title
        self.labelMsg.text = gameState.dialog.message
        self.labelButton.text = gameState.dialog.textButton


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

        # On ajoute le dialog
        self.drawables.append(DialogDrawable(70, 60))

        # On ajoute le gameInfo
        self.drawables.append(GameInfo(700, 80))

        # Turn label
        self.drawables.append(TurnLabel(20, 80))




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

class TurnLabel(Drawable):
    """ Cette classe représente une partie du HUD où le score du joueur sera
        éventuelment affiché.
    """

    def __init__(self, x , y):
        Drawable.__init__(self, x , y)
        self.label = Label('Turn',
                          font_name='Times New Roman',
                          font_size=32,
                          x=x, y=y)


        self.sprites.append(self.label)

    def update(self, gameState):
        self.label.text ="Turn :" + str(gameState.currentTurn())

class GameInfo(Drawable):
    """ Cette classe représente une partie du HUD où le score du joueur sera
        éventuelment affiché.
    """

    def __init__(self, x , y ):
        Drawable.__init__(self, x , y)

    def update(self, gameState):
        dy = 0
        self.sprites = []
        for msg in gameState.infoLog:
            self.sprites.append(Label(msg,
                          font_name='Times New Roman',
                          font_size=18,
                          x=self.x,y=self.y+dy))
            dy -= 22

        if ((self.y+dy) < 0):
            gameState.infoLog.pop(0)


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
                          x=x+(dialogImage.width)/3+30 ,
                          y=y+(dialogImage.height) - 70)
        self.sprites.append(self.labelTitle)

        self.labelMsg1 = Label('Start a new game',
                          font_name='Times New Roman',
                          font_size=24,
                          x=x+40, y=y+(dialogImage.height)-100)
        self.sprites.append(self.labelMsg1)

        self.labelMsg2 = Label('',
                          font_name='Times New Roman',
                          font_size=24,
                          x=x+40, y=y+(dialogImage.height)-126)
        self.sprites.append(self.labelMsg2)

        self.labelButton = Label('Start',
                          font_name='Times New Roman',
                          font_size=28,
                          x=x+(dialogImage.width)/3+10, y=y+75)
        self.sprites.append(self.labelButton)




    def update(self, gameState):
        self.visible = gameState.dialog.visible
        self.labelTitle.text = gameState.dialog.title

        lineLen = 28

        if(len(gameState.dialog.message) > lineLen ):
            self.labelMsg1.text = gameState.dialog.message[0:lineLen ]
            self.labelMsg2.text = gameState.dialog.message[lineLen:]
        else:
             self.labelMsg1.text = gameState.dialog.message
             self.labelMsg2.text = ""

        self.labelButton.text = gameState.dialog.textButton


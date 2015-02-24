""" Autheur Giuseppe Federico 
"""
from pyglet.text import Label
from pyglet.sprite import Sprite
import pyglet


DATA_PATH = "data/"

class HUD:
    """ Cette classe représente un HUD 
    """

    def __init__(self, window):
        # La liste des Sprites qui composent le HUD
        self.sprites = []

        # On initialise un ScoreLabel avec la valeur de l'état de jeu initial et la fenetre
        self.score_label = ScoreLabel(window)
        # Fond vert
        self.background = pyglet.image.load(DATA_PATH + "table/table.jpg")
        self.background = Sprite(self.background,0,0)
        self.sprites.append(self.background)

        # On ajoute le score au hud
        self.sprites.append(self.score_label)



    def update(self, game_state):
        """ Fonction qui va mettre à jour les composants du HUD quand l'état de jeu change
        """

        # On met à jour le ScoreLabel avec le score courant
        score = game_state.agentsStates[0].score
        self.score_label.update(score)

    def getSprites(self):
        return  self.sprites


class ScoreLabel(Label):
    """ Cette classe représente une partie du HUD où le score du joueur sera
        éventuelment affiché.
    """

    #TODO: bien positioner le ScoreLabel par rapport à la résolution de l'écran
    def __init__(self, window):
        super(ScoreLabel, self).__init__('0',
                          font_name='Times New Roman',
                          font_size=36,
                          x=100, y=100)


    def update(self, score):
        self.text = "Score:" + str(score)

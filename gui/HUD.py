""" Autheur Giuseppe Federico 
"""
from pyglet.text import Label

class HUD:
    """ Cette classe représente un HUD 
    """

    def __init__(self, window):
        # La liste des Sprites qui composent le HUD
        self.hud_components = []

        # On initialise un ScoreLabel avec la valeur de l'état de jeu initial et la fenetre
        self.score_label = ScoreLabel(window)

        # On ajoute le score au hud
        self.hud_components.append(self.score_label)

    def update(self, game_state):
        """ Fonction qui va mettre à jour les composants du HUD quand l'état de jeu change
        """

        # On met à jour le ScoreLabel avec le score courant
        score = game_state.agentsStates[0].score
        self.score_label.update(score)




class ScoreLabel(Label):
    """ Cette classe représente une partie du HUD où le score du joueur sera
        éventuelment affiché.
    """

    #TODO: bien positioner le ScoreLabel par rapport à la résolution de l'écran
    def __init__(self, window):
        self.text = "0"
        self.font_name='Times New Roman'
        self.font_size=36
        self.x=window.width//2
        self.y=window.height-20
        self.anchor_x='center'
        self.anchor_y='center'


    def update(self, score):
        self.text = str(score)

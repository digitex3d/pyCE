""" Autheur Giuseppe Federico 
"""
from environment.Table import Table
from gui.Components.Component import Component
from gui.Drawables.CardStackDrawable import CardStackDrawable
from gui.Drawables.TableDrawable import TableDrawable

class TableComponent(Component):
    """ Cette classe représente un TableComponent 
    """

    def __init__(self, win):
        Component.__init__(self, win)
        self.win = win

        # la dimensions de la fenetre
        h = self.win.height
        w = self.win.width

        # Ajout de la table ( conteneur des cartes )
        rw = 1/3*w
        rh = 1/3*h
        tableDrawable = TableDrawable(rw,rh,w-2*rw,h-2*rh)
        self.addDrawable(tableDrawable)

    def setUp(self, gameState):
        """ Toujours appeler cette fonction pour initialiser la table
        :param gameState:
        :return:
        """
        # le dimensions de la fenetre
        h = self.win.height
        w = self.win.width

        # la position de la main
        x = 0
        y = 0
        dir = "h"

        for pid in range(1,gameState.table.nbPlayers):
            # La position de la main du joueur principal
            if( pid == 1):
                x = w/2
                y = h/8
                dir = "h"

             # La position des autre joueurs
            if( pid == 2):
                x = w/2
                y = h*7/8
                dir = "h"

             # La position des autre joueurs
            if( pid == 3):
                x = w*7/8
                y = h/2
                dir = "v"

            # La position des autre joueurs
            if( pid == 4):
                x = w*7/8
                y = h/2
                dir = "v"

            drawableHand = CardStackDrawable(x,y,pid,dir)
            self.drawables.append(drawableHand)

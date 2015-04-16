""" Autheur Giuseppe Federico 
"""
from environment.Table import Table
from gui.Components.Component import Component
from gui.Drawables.CardStackDrawable import CardStackDrawable
from gui.Drawables.DeckDrawable import DeckDrawable
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
        tableDrawable = TableDrawable(240,145,500,500)
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

        # La position des mains des joueurs principal
        for pid in range(gameState.table.nbPlayers):


            if( pid == 0):
                x = 200
                y = 0
                dir = "h"

             # La position des autre joueurs
            if( pid == 1):
                x = 0
                y = 400
                dir = "v"

             # La position des autre joueurs
            if( pid == 2):
                x = 300
                y = h-100
                dir = "h"

            # La position des autre joueurs
            if( pid == 3):
                x = w-100
                y = h-500
                dir = "v"

            drawableHand = CardStackDrawable(x,y,pid,dir)
            self.drawables.append(drawableHand)



        drawableDeck = DeckDrawable(500, 500,-1,"h")
        self.drawables.append(drawableDeck)

        # Position des decks
        for pid in range(gameState.table.nbPlayers):
              # La position de la main du joueur principal
            if( pid == 0):
                x = w-200
                y = 0
                dir = "h"

             # La position des autre joueurs
            if( pid == 1):
                x = 0
                y = 200
                dir = "v"

             # La position des autre joueurs
            if( pid == 2):
                x = 100
                y = h-100
                dir = "h"

            # La position des autre joueurs
            if( pid == 3):
                x = w-100
                y = h-200
                dir = "v"

            drawableDeck = DeckDrawable(x,y,pid,dir)
            self.drawables.append(drawableDeck)

""" Autheur Giuseppe Federico 
"""
import abc

class Component:
    """ Cette classe représente un Component, un component est un ensemble de Drawables
    """

    def __init__(self, win):
        self.drawables = []
        self.window = win

    def addDrawable(self, drawable):
        """
        Ajoute un drawable à la liste des drawables
        :param Drawable:
        :return:
        """
        self.drawables.append(drawable)

    def isClicked(self, x , y):
        """
        Renvoi vrai si un de ses drawables a été clicqué
        :return:
        """
        resu = False
        for drawable in self.drawables:
            resu = resu or drawable.isClicked(x,y)

        return resu

    def getDrawables(self):
        return self.drawables


    def update(self, gameState):
        """
        met à jour les drawables du component
        :param gameState: un etat de jeu
        :return:
        """
       
        for drawable in self.drawables:
            drawable.update(gameState)

    def __str__(self):
        return self.__class__.__name__;
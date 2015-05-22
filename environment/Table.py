# -*- coding: utf-8 -*-
""" Cette classe représente une Table """

from environment.CardStack import CardStack
from game.agents.PlayerState import PlayerState


class Table():

    def __init__(self):
        """
        Cette classe représente l'état d'une table, les joueurs et les cartes sur
        la table.
        :return:
        """
        self.players = []
        self.table = CardStack()
        self.nbPlayers = 0
        self.deck = CardStack()

    def addPlayer(self, hand=CardStack(), deck=CardStack()):
        """
        Fonction qui ajoute un joueur à la table
        :param hand: CardStack la main du joueur à ajouter
        :param deck: CardStack le je du joueur initial
        """

        num = self.nbPlayers
        playerState = PlayerState(num, hand, deck)
        self.nbPlayers += 1
        self.players.append(playerState)

    def getPlayerHand(self, pid):
        """
        Cette fonction renvoie ma main du joueur CardStack à partir d'un pid
        :param pid: int
        :return: CardStack
        """
        return self.players[pid].hand

    def flush(self):
        """ Efface le contenu de la table.
        :return:
        """
        self.table = []

    def __str__(self):
        string = "["
        for index, item in enumerate(self):
            string += str(item)
            if index != len(self)-1:
                string += ", "
        return string + "]"


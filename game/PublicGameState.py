from environment.DeckGenerator import DeckGenerator
from game.GameState import GameState
from game.InitState import InitState
import logging
from gui.Default import TABLE_PID


class PublicGameState:
    """ Cette classe représente un état de jeu pour le dévelopeurs d'un plugin.

    """

    def __init__(self, gameState):
        self.gameState = gameState

    def getCurrentPlayer(self):
        """ Renvoie le joueur courant
        :return:
        """
        self.gameState.getPlayer( self.currentTurn())

    def getCurrentPlayerScore(self):
        """ Renvoie le score du joueur
        :return (int):
        """

        return  self.gameState.getCurrentPlayer().score


    def pid(self, object):
        """ Renvoie le pid d'un objet
        :param object:
        :return: (int) pid
        """
        if( hasattr(object,"getPid()") ):
            return object.getPid()

        else:
            print(object + " ne contient pas un pid.")

    def getTable(self):
        """
        Cette fonction renvoie la table de jeu
        :return: CardStack
        """
        return  self.gameState.table.table


    def getPlayerHand(self, pid):
        """
        Cette fonction renvoie ma main du joueur à partir d'un pid
        :param pid: int
        :return: CardStack
        """
        if (pid == -1 ): return  self.gameState.table.table
        return  self.gameState.table.getPlayerHand(pid)

    def getCurrentPlayerDeck(self):
        """ Renvoie le score du joueur
        :return (int):
        """

        return  self.gameState.table.players[self.currentTurn()].deck

    def win(self):
        """ La partie est gangé
        :return:
        """
        self.gameState.win = True


    def currentTurn(self):
        """
        Renvoie le tour courrant
        :return:
        """
        return  self.gameState.turn

    def getnbPlayers(self):
        return  self.gameState.table.nbPlayers


    def pickCard(self, pid):
        """Déplace une carte du jeu de carte du joueur pid à sa main

        :param pid (int): Le pid du joueur résponsable de l'action
        :return:
        """

        card =   self.gameState.getPlayer(pid).deck.pop()
        self.gameState.getPlayer(pid).hand.append(card)

    def isPlayerTurn(self):
        return  self.gameState.turn == 0

    def flushTable(self):
        """ Efface le contenu de la table
        """

        self.gameState.table.flush()

    def playCard(self, card):
        oc = card
        od = self.currentTurn()
        dd = TABLE_PID

        self.gameState.moveCard(oc, od, dd)

    def getCurrentPlayerHand(self):
        """ Retourne la main du joueur courant

        :return: un CardStack
        """
        return  self.gameState.getPlayerHand(self.currentTurn())

    def getPlayer(self, pid):
        """ Retourne un le PlayerState du joueur (pid)

        :param pid (int): Le pid du joueur que l'on veut obtenir
        :return: un PlayerState
        """
        return  self.gameState.table.players[pid]

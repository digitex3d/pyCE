import copy
import logging
from environment.Dialog import Dialog
from environment.Table import Table

from game.Plugin import InitState
from gui.Default import TABLE_PID


class GameState:
    """ Cette classe représente un état de jeu, elle nécessite une classe qui contient les informations
    de l'état initiale du jeu ( numero de joueurs et ses etats initiaux )
    """

    def __init__(self, init_state, plugin):
        self.win = False
        self.lose = False
        # L'état initial de la table
        self.table = init_state.table
        # l'id du premier joueur qui joue
        self.turn = init_state.turn
        self.plugin = plugin
        self.cardValues = init_state.cardValues
        # Jeu en pause?
        self.paused = True
        self.dialog = init_state.dialog
        self.infoLog = []


    def nextState(self,agent_action):
        """
        Renvoie l'état de jeu étant donné une action
        :param agent_action: AgentAction l'action du joueur
        :return:
        """

        if( self.plugin.GisLegalMove(self, agent_action)):

            return self.plugin.GNextState(self, agent_action)
        else:
            logging.debug("Illegal move")
            self.infoLog.append("Illegal Move!")
            return self

    def getCurrentPlayer(self):
        """ Renvoie le joueur courant
        :return:
        """
        self.getPlayer( self.currentTurn())

    def getCurrentPlayerScore(self):
        """ Renvoie le score du joueur
        :return (int):
        """

        return self.getCurrentPlayer().score


    def getPlayerHand(self, pid):
        """
        Cette fonction renvoie ma main du joueur à partir d'un pid
        :param pid: int
        :return: CardStack
        """
        if (pid == -1 ): return self.table.table
        return self.table.getPlayerHand(pid)

    def getCurrentPlayerHand(self):
        return self.table.getPlayerHand(self.currentTurn()).hand

    def getCurrentPlayerDeck(self):
        """ Renvoie le score du joueur
        :return (int):
        """

        return self.table.players[ self.turn].deck

    def win(self):
        """ La partie est gangé
        :return:
        """
        self.win = True

    def lose(self):
        """ La partie est perdue
        :return:
        """
        self.lose = True

    def moveCard(self, card, orig, dest):
        """
        Bouge une carte d'un CardStack initial dans un CardStack finale
        :param card: Card
        :param orig: int pid
        :param dest: int pid
        :return:
        """

        logging.debug("Origin pid: %s", orig)
        logging.debug("Destination pid: %s", dest)

        logging.debug("Origin: %s",  self.getPlayerHand(orig))
        logging.debug("Destination: %s", self.getPlayerHand(dest))
        logging.debug("Card: %s", card)

        self.getPlayerHand(orig).remove(card)
        self.getPlayerHand(dest).append(card)


    def currentTurn(self):
        """
        Renvoie le tour courrant
        :return:
        """
        return self.turn

    def getnbPlayers(self):
        return self.table.nbPlayers

    def next_turn(self):
        """ Fonction qui passe le tourne
        """
        nb = self.getnbPlayers()
        tmp = (self.turn+1)
        resu = tmp % nb
        self.turn = resu

    def pickCard(self, pid):
        """Déplace une carte du jeu de carte du joueur pid à sa main

        :param pid (int): Le pid du joueur résponsable de l'action
        :return:
        """

        card =  self.getPlayer(pid).deck.pop()
        self.getPlayer(pid).hand.append(card)

    def isPlayerTurn(self):
        return self.turn == 0

    def flushTable(self):
        """ Efface le contenu de la table
        """

        self.table.flush()

    def playCard(self, card):
        oc = card
        od = self.currentTurn()
        dd = TABLE_PID

        self.moveCard(oc, od, dd)

    def getCurrentPlayerHand(self):
        """ Retourne la main du joueur courant

        :return: un CardStack
        """
        return self.getPlayerHand(self.currentTurn())

    def getPlayer(self, pid):
        """ Retourne un le PlayerState du joueur (pid)

        :param pid (int): Le pid du joueur que l'on veut obtenir
        :return: un PlayerState
        """
        return self.table.players[pid]


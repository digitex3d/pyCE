""" Autheur Giuseppe Federico 
"""
from game.InitState import InitState
from game.PublicGameState import PublicGameState
from game.agents.AgentAction import AgentAction
from game.agents.Player import Player


class Plugin:
    """ Cette classe représente un Plugin 
    """


    def __init__(self):
        test = True
        self.TABLE_PID = -1
        self.PLAYER_PID = 0
        self.opponents = []
        # Initialisation du jeu
        self.initState = InitState()
        self.gameState = None
        self.agentAction = None

    def nextState(self, gameState, agent_action):
        """ Classe abstraite à implémenter dans le plugin.
        :return:
        """
        return None

    def GNextState(self, gameState, agent_action):
        new_state = gameState.copy()
        self.gameState = new_state
        self.agentAction = agent_action
        self.nextState()
        return self.gameState

    def GisLegalMove(self, gameState, agent_action):
        new_state = gameState.copy()
        self.gameState = new_state
        self.agentAction = agent_action
        return self.isLegalMove()


    def getAction(self):
        return self.agentAction

    def getTable(self):
        """
        Cette fonction renvoie la table de jeu
        :return: CardStack
        """
        return self.gameState.table

    def getTableCards(self):
        """
        Cette fonction renvoie les cartes de la table
        :return: CardStack
        """
        return self.gameState.table.table


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
        dd = self.TABLE_PID

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

    def getAction(self):
        return self.agentAction

    def next_turn(self):
        """ Fonction qui passe le tourne
        """
        nb = self.gameState.getnbPlayers()
        tmp = (self.gameState.turn+1)
        resu = tmp % nb
        self.gameState.turn = resu


class IAPlugin(Player):
    def __init__(self, id):
        Player.__init__(self, id)

    def getAction(self, agent_state, gameState, event=None):
        return None

    def defAgentAction(self, id , type):
        return AgentAction(id, type)


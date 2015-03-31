from game.InitState import InitState
import logging

class GameState:
    """ Cette classe représente un état de jeu, elle nécessite une classe qui contient les informations
    de l'état initiale du jeu ( numero de joueurs et ses etats initiaux )
    """

    def __init__(self, init_state, plugin):
        self.win = False

        # L'état initial de la table
        self.table = init_state.table
        # l'id du premier joueur qui joue
        self.turn = init_state.turn
        self.plugin = plugin

    def nextState(self, agent_action):
        """
        Renvoie l'état de jeu étant donné une action
        :param agent_action: AgentAction l'action du joueur
        :return:
        """
        if( self.plugin.isLegalMove(self, agent_action)):

            return self.plugin.nextState(self, agent_action)
        else:
            logging.debug("Illegal move")
            return self.copy()

    def getPlayerHand(self, pid):
        """
        Cette fonction renvoie ma main du joueur à partir d'un pid
        :param pid: int
        :return: CardStack
        """
        if (pid == -1 ): return self.table.table
        return self.table.getPlayerHand(pid)

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

        logging.debug("Origin: %s",  self.table.players[orig].hand)
        logging.debug("Destination: %s", self.table.players[dest].hand)
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

    def isPlayerTurn(self):
        return self.turn == 0

    def copy(self):
        new_init = InitState()
        new_init.turn = self.turn
        new_init.table = self.table
        new_init.win = self.win

        state_copy = GameState(  new_init , self.plugin)
        return state_copy

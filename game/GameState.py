from game.InitState import InitState
import logging

class GameState:
    """ Cette classe représente un état de jeu, elle nécessite une classe qui contient les informations
    de l'état initiale du jeu ( numero de joueurs et ses etats initiaux )
    """

    def __init__(self, plugin):
        self.win = False

        init_state = plugin.initGameState()
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
        return self.plugin.nextState(self, agent_action)

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



    def isLegalMove(self, agent_action):
        #TODO: à implémenter
        """
        Renvoie True si l'action est legale dans l'état courant
        :param agent_action:
        :param plugin:
        :return:
        """
        return self.plugin.isLegalMove(self, agent_action)

    def next_turn(self):
        """ Fonction qui passe le tourne
        """
        self.turn = ++self.turn % self.nb_players

    def isPlayerTurn(self):
        return self.turn == 0

    def copy(self):
        new_init = InitState()
        new_init.turn = self.turn
        new_init.table = self.table
        new_init.win = self.win

        state_copy = GameState( new_init )
        return state_copy

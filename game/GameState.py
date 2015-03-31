from game.InitState import InitState


class GameState:
    """ Cette classe représente un état de jeu, elle nécessite une classe qui contient les informations
    de l'état initiale du jeu ( numero de joueurs et ses etats initiaux )
    """

    def __init__(self, init_state):
        self.win = False
        # L'état initial de la table
        self.table = init_state.table
        # l'id du premier joueur qui joue
        self.turn = init_state.turn

    def nextState(self, agent_action):
        #TODO: à implémenter
        """  Renvoie le prochain etat du jeu etant donnée une action
        """

        new_state = self.copy()

        # Boujer une carte
        if(agent_action.type == "move"):
            oc = agent_action.origin_card;
            od = agent_action.origin_deck;
            dd = agent_action.dest_deck;

            self.moveCard(oc, od, dd)


        return new_state

    def getPlayerHand(self, pid):
        """
        Cette fonction renvoie ma main du joueur à partir d'un pid
        :param pid: int
        :return: CardStack
        """
        if (pid == 0 ): return self.table.table
        return self.table.getPlayerHand(pid)

    def moveCard(self, card, orig, dest):
        """
        Bouge une carte d'un CardStack initial dans un CardStack finale
        :param card: Card
        :param orig: int pid
        :param dest: int pid
        :return:
        """

        origStack = self.getPlayerHand(orig)
        destStack = self.getPlayerHand(dest)

        origStack.remove(card);
        destStack.append(card);

    def isLegalMove(self, agent_action, plugin):
        #TODO: à implémenter
        """
        Renvoie True si l'action est legale dans l'état courant
        :param agent_action:
        :param plugin:
        :return:
        """
        return True

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

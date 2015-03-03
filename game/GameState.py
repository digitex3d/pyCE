from game.InitState import InitState


class GameState:
    """ Cette classe représente un état de jeu, elle nécessite une classe qui contient les informations
    de l'état initiale du jeu ( numero de joueurs et ses etats initiaux )
    """

    def __init__(self, init_state):
        self.win = False
        self.nb_players = init_state.nb_agents
        self.agentsStates = init_state.agentsStates
        # l'id du premier joueur à jouer
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

            od.remove(oc);
            dd.append(oc);


        if(new_state.agentsStates[0].score > 10):
            new_state.win = True

        return new_state



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
        for agent in  self.agentsStates:
            new_init.addAgentState(agent)

        state_copy = GameState( new_init )
        return state_copy

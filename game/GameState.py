

class GameState:
    """ Cette classe représente un état de jeu
    """

    def __init__(self):
        self.win = False
        self.players_in_game = 0
        self.playerState = None
        self.opponents = []
        # L'agent du joueur principal
        self.player_agent = None


    def add_player(self, pstate):
        """ On ajoute l'état initial de l'agent
        """
        self.player_state = pstate

    def nextState(self, agent_action):
        #TODO: à implémenter
        """
        Renvoie le prochain etat du jeu etant donnée une action
        :param agent_action:
        :return:
        """

        """new_state = self.copy()
        if( isLegalMove(agent_action) )
            updateGame(agent_action)
        else
            return self

            renvoie le prochain etat etant donn
        """


    def isLegalMove(self, agent_action, plugin):
        #TODO: à implémenter
        """
        Renvoie True si l'action est legale dans l'état courant
        :param agent_action:
        :param plugin:
        :return:
        """
        return True




class GameState:
    """ Cette classe représente un état de jeu
    """

    def __init__(self, int):
        self.win = False
        self.players_in_game = 0;
        self.playerState = None


    def nextState(self, agent_action):
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
        """
        Renvoie True si l'action est legale dans l'état courant
        :param agent_action:
        :param plugin:
        :return:
        """
        return True


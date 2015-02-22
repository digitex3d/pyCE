class Game:
    """ Cette classe représente un jeu
        humanPlayer: Agent du joueur humain
    """
    def __init__(self, state):
        # Les observeurs du jeu
        self.observers = []
        self.state = state
        self.player_agent = None

    def addPlayerAgent(self, player_agent):
        """ On ajoute l'agent du joueur ici
        """
        self.player_agent = player_agent

    def addOpponent(self, opponent_agent):
        """ On ajoute un adversaire
        """


    def run(self):
        isPlayerTurn = True
        while((self.state.isLose()==False) and
                  (self.isWin()==False)):
            pactions = []

            # Le tourn du joueur
            if(isPlayerTurn):
                a_state = self.state.playerState
                pactions.append( self.humanPlayer.getAction(a_state, self.state) )

            # On met à jour tous les observateurs du jeu
            for observer in self.observers:
                observer.update(self.state)

        return self.state

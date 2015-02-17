class Game:
    """ Cette classe représente un jeu
        humanPlayer: Agent du joueur humain
    """
    def __init__(self, state, humanPlayer):
        self.observers = []
        self.state = state
        self.humanPlayer = humanPlayer

    def run(self):
        isPlayerTurn = True
        while((self.state.isLose()==False) and
                  (self.isWin()==False)):
            pactions = []
            if(isPlayerTurn):
                a_state = self.state.playerState
                pactions.append( self.humanPlayer.getAction(a_state, self.state) )

            for observer in self.observers:
                observer.update(self.state)

        return self.state

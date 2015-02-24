class Game:
    """ Cette classe représente un jeu
        humanPlayer: Agent du joueur humain
    """
    def __init__(self, state):
        # Les observeurs du jeu
        self.observers = []
        self.game_state = state
        self.agents = []

    def addAgent(self, agent):
        """ On ajoute un agent ici
        """
        self.agents.append(agent)

    def addObserver(self, observer):
        """ Ajoute des observateurs à la liste des observateurs
        """
        self.observers.append(observer)


    def eventHandler(self, event):
        """ Cette classe va gérer tous les événements
        """

        # Si ce n'est pas le tourne du joueur on a rien à gerer
        if( not self.game_state.isPlayerTurn()): return

        # Fonction qui va gerer un click
        if(event.type == "mouse_click"):
            self.handleClick(event)

        # On met à jour tous les observateurs du jeu
        for observer in self.observers:
            observer.update(self.game_state)

    def handleClick(self, event):
        turn = self.game_state.turn
        # Un cylce du jeu
        a_state = self.game_state.agentsStates[turn]

        agent_action = self.agents[turn].getAction(a_state, self.game_state)

        # Effectue l'action et met à jour l'état du jeu
        self.game_state = self.game_state.nextState(agent_action)
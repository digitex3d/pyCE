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


        # L'etat de l'agent qui doit jouer
        a_state = self.game_state.table.players[turn]


        agent_action = self.agents[self.game_state.turn].getAction(a_state, self.game_state, event)

        # Effectue l'action et met à jour l'état du jeu
        self.game_state = self.game_state.nextState(agent_action)

        self.game_state.next_turn()

        agent_action = self.agents[self.game_state.turn].getAction(a_state, self.game_state, event)

         # Effectue l'action et met à jour l'état du jeu
        self.game_state = self.game_state.nextState(agent_action)
        self.game_state.next_turn()





    def isPlayerTourn(self):
        return (self.game_state.turn == 0)
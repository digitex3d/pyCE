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


    def run(self):
        i = 0
        turn_agent_id = i
        while( self.game_state.win == False):

            # Un cylce du jeu
            a_state = self.game_state.agentsStates[turn_agent_id]

            agent_action = self.agents[turn_agent_id].getAction(a_state, self.game_state)

            # Effectue l'action et met à jour l'état du jeu
            self.game_state = self.game_state.nextState(agent_action)

            # On met à jour tous les observateurs du jeu
            for observer in self.observers:
                observer.update(self.game_state)

            # On incrèmente le id du tour de l'agent
            turn_agent_id = i % self.game_state.nb_agents
            i += 1

        return self.state

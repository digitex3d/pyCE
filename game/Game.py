import time
from game.agents.AgentAction import AgentAction


class Game:
    """ Cette classe représente un jeu
        humanPlayer: Agent du joueur humain
    """
    def __init__(self, state):
        # Les observeurs du jeu
        self.observers = []
        self.game_state = state
        self.agents = []
        self.lastEvent = None


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

        # Fonction qui va gerer un click
        if(event.type == "mouse_click"):
            self.handleClick(event)

    def handleLastEvent(self):
        tmp = self.lastEvent
        self.lastEvent = None
        return tmp

    def handleClick(self, event):
        self.lastEvent = event

    def updateGame(self):
        if(self.game_state.paused):
            if( self.lastEvent == None): return
            if ( self.lastEvent.drawableClicked.name == "Dialog" and
                    self.game_state.dialog.action == "unPause"):
                self.game_state.paused = False
                self.lastEvent = None

                return

        if( self.game_state.turn==0 ):
            if( self.lastEvent == None):
                player_action = AgentAction("none")
            else:
                player_action = self.agents[0].getAction(self.game_state, self.handleLastEvent())
        else:
            # L'etat de l'agent qui doit jouer
            turn = self.game_state.turn
            pstate = self.game_state.table.players[turn]
            player_action = self.agents[self.game_state.turn].PgetAction(pstate, self.game_state.plugin)

        # Effectue l'action et met à jour l'état du jeu
        self.game_state = self.game_state.nextState(player_action)

        # On met à jour tous les observateurs du jeu
        self.updateObserver()


    def updateObserver(self):
        # On met à jour tous les observateurs du jeu
        for observer in self.observers:
            observer.update(self.game_state)




    def isPlayerTourn(self):
        return (self.game_state.turn == 0)
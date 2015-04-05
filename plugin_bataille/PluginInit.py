""" Autheur Giuseppe Federico
"""
from game.Plugin import Plugin
from game.agents.Player import Player
from game.agents.AgentAction import AgentAction

class PluginInit():
    """ Cette classe représente un PluginBataille
    """

    def __init__(self):
        Plugin.__init__(self)


    def initGameState(self):
        """ Cette fonction initialise l'état intitial du jeu
            La table et les joueurs.

        """

        deck = self.initState.generateShuffledDeck()

        # Initialisation du joueur1
        ##### INIT PLAYER 1 ######
        deck1 = deck[0:int(len(deck)/2)]
        deck2 = deck[int(len(deck)/2):len(deck) ]

        self.initState.addPlayerState(deck=deck1)
        ###########################

        ##### INIT PLAYER 2 ######

        self.initState.addPlayerState(deck=deck2)
        ###########################

        ######## INIT OPPONENT ##########
        self.opponents.append( IABataille() )
        #################################

        return self.initState



    def nextState(self, gameState, agent_action):
        """  Renvoie le prochain etat du jeu etant donnée une action
        """


        new_state = gameState.copy()

        table = gameState.getTableCards()
        if(len(table) == 2):
            carte1 = table[0]
            carte2 = table[1]
            if(carte1.value > carte2.value):

                gameState.getTable().players[0].score += carte1.value +carte2.value
            else:
                gameState.getTable().players[1].score += carte1.value +carte2.value
            gameState.flushTable()
            deck = gameState.getCurrentPlayerDeck()
            if( len(deck) == 0):
                if( gameState.getPlayer(0).score > gameState.getPlayer(1).score  ):
                    gameState.win()

        for action in agent_action:
            # Tirer une carte
            if( action.type == "pick"):
                gameState.pickCard(gameState.currentTurn())
                hand = gameState.getCurrentPlayerHand()
                gameState.playCard(hand[0])
                new_state.next_turn()

        return new_state


    def isLegalMove(self, gameState, agent_action):
        #TODO: à implémenter
        """
        Renvoie True si l'action est legale dans l'état courant
        :param agent_action:
        :param plugin:
        :return:
        """

        for action in agent_action:
            if(action.type == "move"):
                return False
            if(action.type == "pick"):
                return len(gameState.getCurrentPlayerDeck()) > 0


        return True

class IABataille(Player):
    def __init__(self):
        Player.__init__(self, 1)

    def getAction(self, agent_state, gameState, event=None):
        actions = []
        pick = AgentAction(self.id, "pick")
        actions.append(pick)
        return actions


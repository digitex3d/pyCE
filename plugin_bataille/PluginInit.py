""" Autheur Giuseppe Federico
"""
from game.Plugin import Plugin, IAPlugin


class PluginInit(Plugin):
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



    def nextState(self):
        """  Renvoie le prochain etat du jeu etant donnée une action
        """

        table = self.getTableCards()

        if(len(table) == 2):
            carte1 = table[0]
            carte2 = table[1]
            if(carte1.value > carte2.value):

                self.getPlayer(0).score += carte1.value +carte2.value
            else:
                self.getPlayer(1).score += carte1.value +carte2.value
            self.flushTable()
            deck = self.getCurrentPlayerDeck()
            if( len(deck) == 0):
                if( self.getCurrentPlayer.score > self.getPlayer(1).score  ):
                    self.win()

        for action in self.getAction():
            # Tirer une carte
            if( action.type == "pick"):
                self.pickCard(self.currentTurn())
                hand = self.getCurrentPlayerHand()
                self.playCard(hand[0])
                self.next_turn()



    def isLegalMove(self):
        #TODO: à implémenter
        """
        Renvoie True si l'action est legale dans l'état courant
        :param agent_action:
        :param plugin:
        :return:
        """

        for action in self.agentAction:
            if(action.type == "move"):
                return False
            if(action.type == "pick"):
                return len(self.getCurrentPlayerDeck()) > 0



        return True

class IABataille(IAPlugin):
    def __init__(self):
        IAPlugin.__init__(self, 1)

    def getAction(self, agent_state, gameState, event=None):
        actions = []
        pick = self.defAgentAction(self.id, "pick")
        actions.append(pick)
        return actions


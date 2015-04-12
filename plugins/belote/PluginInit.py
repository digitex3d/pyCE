""" Autheur Giuseppe Federico
"""
from game.Plugin import Plugin, IAPlugin


class PluginInit(Plugin):
    """ Cette classe représente un Plugin pour jouer à la belote
    """

    def __init__(self):
        Plugin.__init__(self)
        self.isFirstTurn = True


    def initGameState(self):
        """ Cette fonction initialise l'état intitial du jeu
            La table et les joueurs.

        """

        # Renvoie un jeu de cartes mélangé
        deck = self.initState.generateShuffledDeck()


        self.initState.setTableDeck(deck)
        # Initialisation des joueurs

        #Player1 id=0
        self.initState.addPlayerState()

        #Player2 id=1
        self.initState.addPlayerState()

        #Player3 id=2
        self.initState.addPlayerState()

        #Player4 id=3
        self.initState.addPlayerState()

        # Initialise les adversaires
        self.opponents.append( IABelote(1) )
        self.opponents.append( IABelote(2) )
        self.opponents.append( IABelote(3) )

        return self.initState



    def nextState(self):
        """  Renvoie le prochain etat du jeu etant donnée une action
            getAction() pour récuperer une action
        """

        #if(self.isFirstTurn):
        #    self.dealCards(self.TABLE_PID, 10)
        #    self.isFirstTurn=False

        for action in self.getAction():
            # Tirer une carte
            if( action.type == "pick"):
                self.pickCardFrom(self.TABLE_PID)
            if( action.type == "move"):
                self.playCard(action.originSprite)
                self.next_turn()


    def isLegalMove(self):
        #TODO: à implémenter
        """
        Renvoie True si l'action est legale dans l'état courant
        :param agent_action:
        :param plugin:
        :return:
        """

        for action in self.getAction():
            if(action.type == "pick"):
                od = action.originDrawable
                if( od != None and od.name == "CardStack"):
                    if( action.originDrawable.pid != self.getCurrentPlayer()):
                        return False




        return True

class IABelote(IAPlugin):
    def __init__(self, id ):
        IAPlugin.__init__(self, id)

    def getAction(self, agent_state, gameState, event=None):
        actions = []
        pick = self.defAgentAction(self.id, "pick")
        actions.append(pick)
        return actions


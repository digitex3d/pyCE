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

            Toutes les initialisations doivent modifier l'objet
            initState.
        """

        # Affecte la valeur des cartes {carte:valeur}
        valeurs = {
            1:1,
            2:2,
            3:3,
            4:4,
            5:5,
            6:6,
            7:7,
            8:8,
            9:9,
            10:10,
            11:11,
            12:12,
            13:13,
            14:14
        }

        self.initState.setCardValues(valeurs)

        # Renvoie un jeu de cartes mélangé
        deck = self.initState.generateShuffledDeck()

        # Initialisation des joueurs

        deck1 = deck[0:int(len(deck)/2)]
        deck2 = deck[int(len(deck)/2):len(deck)]

        #Player1 id=0
        self.initState.addPlayerState(deck=deck1)

        #Player2 id=1
        self.initState.addPlayerState(deck=deck2)

        # Initialise un adversaire ( le premier adversaire a le pid = 1)
        self.opponents.append( IABataille() )

        return self.initState



    def nextState(self):
        """  Renvoie le prochain etat du jeu etant donnée une action
            getAction() pour récuperer une action
        """

        if( len(self.getAction())==0 ): return
        if( not self.isLost() and not self.isWin()):
            table = self.getTableCards()

            if(len(table)!=0 and len(table)%2 == 0):
                carte1 = table[len(table)-2]
                carte2 = table[len(table)-1]
                finalscore = 0
                cards_index = 0

                carte1Val = self.getValeurCarte(carte1)
                carte2Val = self.getValeurCarte(carte2)

                if((carte1Val != carte2Val)):
                    if( carte1.value > carte2.value):
                        self.getPlayer(0).score += carte1Val +carte2Val + finalscore
                    else:
                        self.getPlayer(1).score += carte1Val +carte2Val + finalscore
                    self.flushTable()
                else:
                    finalscore += carte1Val +carte2Val

        for action in self.getAction():
            # Tirer une carte
            if( action.type == "pick"):
                self.pickCardFrom(self.currentTurn())
                hand = self.getCurrentPlayerHand()
                self.playCard(hand[0])
                self.next_turn()
            else:
                return

        deck = self.getCurrentPlayerDeck()
        if( len(deck) == 0):
            if( self.getPlayer(0).score > self.getPlayer(1).score  ):
                self.win()
                return
            elif ( self.getPlayer(0).score < self.getPlayer(1).score  ):
                self.lose()
                return
            else:
                return



    def isLegalMove(self):
        #TODO: à implémenter
        """
        Renvoie True si l'action est legale dans l'état courant
        :param agent_action:
        :param plugin:
        :return:
        """

        for action in self.getAction():
            if(action.type == "move"):
                return False
            if(action.type == "pick"):
                od = action.originDrawable
                if( od != None and od.name == "CardStack"):
                    if( action.originDrawable.pid != self.getCurrentPlayer()):
                        return False




        return True

class IABataille(IAPlugin):
    def __init__(self):
        IAPlugin.__init__(self, 1)

    def getAction(self, agent_state, gameState, event=None):
        actions = []
        pick = self.defAgentAction(self.id, "pick")
        actions.append(pick)
        return actions


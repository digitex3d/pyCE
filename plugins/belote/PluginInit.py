""" Autheur Giuseppe Federico
"""
from game.Plugin import Plugin, IAPlugin


class PluginInit(Plugin):
    """ Cette classe représente un PluginBataille
    """

    def __init__(self):
        Plugin.__init__(self, "La Belote")
        self.atout=None



    def pluginInit(self):
        """ Cette fonction initialise l'état intitial du jeu
            La table et les joueurs.

            Toutes les initialisations doivent modifier l'objet
            initState.
        """

        self.initPlayers(4)
        self.opponents.append(IABelote())


    def initialPhase(self):
        # Enlève les cartes qui sont pas utilisées
        self.removeRangeOfCards(self.getTableDeck(), 2,6, ['h','c','s','d'] )
        self.dealCards(5)
        self.dealToTable(1)
        self.showDialogMessage("Take", "Take? ", "No" )
        self.setCurrentPhase("Take")

    def takePhase(self):
        action = self.getAction()
        if(action.type == "move"):
            card = self.getSelectedCard()
            self.atout = card.kind
            self.showDialogMessage("Info", "Trump has been chosen."+ self.atout, "Ok" )

            # Distribution du reste des cartes
            for i in range(self.getnbPlayers()):
                if (i != self.currentTurn()):
                    self.dealTo(i, 4)
                else:
                    self.dealTo(i, 3)
                    card = self.getTable().pop()
                    self.appendCardToMyHand(card)

            self.setCurrentPhase("Play")
            self.next_turn()
        if(action.type == "dialog"):
            if(self.lastPlayerToPlay()):
                self.showDialogMessage("Info", "Trump has not been chosen, restarting.", "Ok")
                self.resetTable()
                self.initialPhase()
        self.next_turn()



    def playPhase(self):
        self.flushTable()
        self.playSelectedCard()
        if(self.lastPlayerToPlay()):
            self.endTurnPhase()
        else:
            self.setCurrentPhase("Play")

        self.next_turn()

    def dealPhase(self):
        self.dealCards(1)
        self.setCurrentPhase("Play")

    def isWin(self):
        if( self.isDeckEmpty() and self.IHaveBestScore()):
            return True
        else: False


    def isLost(self):
        if( self.isDeckEmpty() and not self.IHaveBestScore()):
            return True
        else: False

    def endTurnPhase(self):
        lastCards = self.getLastCards(2)

        carte1Val = self.getValeurCarte(lastCards[0])
        carte2Val = self.getValeurCarte(lastCards[1])

        if((carte1Val != carte2Val)):
            score = self.getTableSumCardScore()
            if( carte1Val > carte2Val):
                self.addPlayerScore(0, score)
                self.showDialogMessage("End Turn", "Player 1 win turn. Points:"
                                       + str(score), "Ok" )
            else:
                self.addPlayerScore(1, score)
                self.showDialogMessage("End Turn", "Player 2 win turn. Points: "
                                       + str( score ), "Ok" )
            self.setCurrentPhase("Start")

        else:
            self.showDialogMessage("End Turn", "Draw", "Ok" )
            self.setCurrentPhase("Deal")






    def nextState(self):
        """  Renvoie le prochain etat du jeu etant donnée une action
            getAction() pour récuperer une action
        """

        # On récupere la phase de jeu actuelle
        phase = self.getCurrentPhase()

        # Le jeu commence toujours par la phase Start
        if( phase == "Start"):
            self.initialPhase()

        if( phase == "Take"):
            self.takePhase()

        if( phase == "EndTurn"):
            self.endTurnPhase()

        if( phase == "Deal"):
            self.dealPhase()

    def isLegalMove(self):
        #TODO: à implémenter
        """
        Renvoie True si l'action est legale dans l'état courant
        :param agent_action:
        :param plugin:
        :return:
        """

        return True

class IABelote(IAPlugin):
    def __init__(self):
        IAPlugin.__init__(self, 1)


    def getAction(self, plugin):
        if(plugin.getCurrentPhase() == "Take"):
            return self.takePhase(plugin)

    def takePhase(self, plugin):
        card = plugin.getCardFromTable(0)
        cardValue = plugin.getValeurCarte(card)
        if( cardValue > 11 ):
            return plugin.defAgentAction("move", card)
        else:
            return plugin.defAgentAction("dialog", card)

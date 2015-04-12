""" Autheur Giuseppe Federico
"""
from game.Plugin import Plugin, IAPlugin


class PluginInit(Plugin):
    """ Cette classe représente un PluginBataille
    """

    def __init__(self):
        Plugin.__init__(self, "La Bataille")



    def pluginInit(self):
        """ Cette fonction initialise l'état intitial du jeu
            La table et les joueurs.

            Toutes les initialisations doivent modifier l'objet
            initState.
        """

        self.initPlayers(2)
        self.opponents.append(IABataille())


    def initialPhase(self):
        self.flushTable()
        self.dealCards(1)
        self.setCurrentPhase("Play")

    def playPhase(self):
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

        if( phase == "Play"):
            self.playPhase()

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

class IABataille(IAPlugin):
    def __init__(self):
        IAPlugin.__init__(self, 1)


    def getAction(self, plugin):
        card = plugin.getCurrentPlayerFirstCard()
        move = plugin.defAgentAction("move", originSprite=card)
        return move


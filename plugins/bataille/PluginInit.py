""" Autheur Giuseppe Federico
"""
from game.PluginManager import PluginManager, IAPlugin


class PluginInit(PluginManager):
    """ Cette classe représente un PluginBataille
    """

    def __init__(self):
        PluginManager.__init__(self, "La Bataille")



    def pluginInit(self):
        """ Cette fonction initialise l'état intitial du jeu
            La table et les joueurs.
        """

        self.initPlayers(2)
        self.opponents.append(IABataille())


    def initialPhase(self):
        self.flushTable()

        # Distribution des cartes aux joueurs
        self.dealCards(1)

        # On affecte le premier joueur
        self.setFirstPlayer(0)


        # On affecte le dérnier joueur
        self.setLastPlayer(1)

        # On change de phase de jeu
        self.setCurrentPhase("Play")

    def playPhase(self):
        if(self.agentAction.type == "move"):
            self.playSelectedCard()
            if(self.iAmLastPlayerToPlay()):
                self.endTurnPhase()
            else:
                self.setCurrentPhase("Play")

            self.next_turn()


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
            winner = 0 if (carte1Val > carte2Val) else 1
            self.addPlayerScore(winner, score)
            self.appendLogInfoMessage("Player " + str(winner) + " win turn. Points:" + str(score))
            self.setCurrentPhase("Start")
        else:
            self.appendLogInfoMessage("Draw")
            self.dealCards(1)
            self.setCurrentPhase("Play")


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


    def isLegalMove(self):
        """
        Renvoie True si l'action est legale dans l'état courant
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


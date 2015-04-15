""" Autheur Giuseppe Federico
"""
from random import randint
from game.Plugin import Plugin, IAPlugin


class PluginInit(Plugin):
    """ Cette classe représente un PluginBataille
    """

    def __init__(self):
        Plugin.__init__(self, "La Belote")
        self.atout=None

        self.cartesAtout = {
            1:11,
            7:0,
            8:0,
            9:14,
            10:10,
            11:20,
            12:3,
            13:4,
        }

        self.cartesNAtout = {
            1:11,
            7:0,
            8:0,
            9:0,
            10:10,
            11:2,
            12:3,
            13:4,
        }


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

        # Les joueurs reçoivent chacun 5 cartes.
        self.dealCards(5)

        self.choseRandomDealer()

        # Une carte est placée, face découverte, au milieu de la table de jeu.
        self.dealToTable(1)

        # Le premier joueur à jouer
        self.setFirstPlayer(self.getLeftPlayerOf(self.getDealerPID()))
        self.setLastPlayer(self.getDealerPID())
        self.setCurrentTurn(self.getFirstPlayer())


        self.showDialogMessage("Info", "Chosing trump phase.", "Ok" )
        self.setCurrentPhase("Take")


    def dealTrumpCards(self):
        # Distribution du reste des cartes
        for i in range(self.getnbPlayers()):
            if (i != self.currentTurn()):
                self.dealTo(i, 3)
            else:
                self.dealTo(i, 2)
                card = self.popCardFromTable()
                self.appendCardToMyHand(card)

    def takePhase(self):
        action = self.getAction()
        print("Atction type:" + action.type)

        if( action.type == "none" ):
            self.showDialogAction("Info", "Chose this trump?", "no", "pass" )
            return

        print(" Is chosing atout"+str(self.currentTurn()))
        print("Atction type after:" + action.type)

        if(action.type == "move"):
            card = self.getSelectedCard()
            self.atout = card.kind
            self.dealTrumpCards()
            self.initPlayPhase()
            self.showDialogMessage("Info", "Trump has been chosen."+ self.atout, "Ok" )
            print("Atout choisi" + self.atout)

        if(action.type == "pass"):
            if(self.iAmLastPlayerToPlay()):
                self.showDialogMessage("Info", "Chose trump manual", "ok" )
                print("Choix manual attout")
                self.initTake2phase()
        self.next_turn()


    def initPlayPhase(self):
         # Le premier joueur à jouer
        self.flushTable()
        self.setFirstPlayer(self.getLeftPlayerOf(self.getDealerPID()))
        self.setLastPlayer(self.getDealerPID())
        self.setCurrentTurn(self.getFirstPlayer())
        self.setCurrentPhase("Play")

    def take2Phase(self):
        action = self.getAction()
        print("Atction type:" + action.type)

        if( action.type == "none" ):
            self.showDialogAction("Info", "Chose a trump or pass", "pass", "pass" )
            return

        print(" im playinggn"+str(self.currentTurn()))
        print("Atction type after:" + action.type)

        if(action.type == "move"):
            card = self.getSelectedCard()
            self.atout = card.kind
            self.showDialogMessage("Info", "Trump has been chosen."+ self.atout, "Ok" )
            self.dealTrumpCards()
            self.initPlayPhase()
        if(action.type == "pass"):
            if(self.iAmLastPlayerToPlay()):
                self.resetTable()
                self.setCurrentTurn(0)
                self.getCurrentPhase("Start")
                self.flushTable()
                self.showDialogMessage("Info", "Trump has not been chosen restarting.", "Ok" )
            self.showDialogMessage("Info", "Discarding.", "Ok" )
        self.next_turn()

    def playPhase(self):
        action = self.getAction()
        print("Atction type ndaplay:" + action.type)
        print(" im playinggn ndaplay"+str(self.currentTurn()))
        if( action.type == "none" ):
            return

        self.playSelectedCard()
        if(self.iAmLastPlayerToPlay()):
            self.endTurnPhase()
            return
        self.next_turn()


    def isWin(self):
        return False


    def isLost(self):
        return False

    def endTurnPhase(self):
        totalScore = self.getTableSumCardScore()
        winner = self.getTableBestCardOwner()
        self.addPlayerScore(winner, totalScore)
        self.setFirstPlayer(winner)
        self.setLastPlayer(self.getRightPlayerOf(winner))
        self.setCurrentTurn(winner)
        self.setCurrentPhase("Play")
        self.showDialogMessage("Info", "Hand winner is " + str(winner), "Ok" )
        self.flushTable()


    def initTake2phase(self):
        h = self.defCard(1,'h')
        s = self.defCard(1,'s')
        c = self.defCard(1,'c')
        d = self.defCard(1,'d')
        self.appendCardToTable(h)
        self.appendCardToTable(s)
        self.appendCardToTable(c)
        self.appendCardToTable(d)
        self.setCurrentPhase("Take2")
        self.setFirstPlayer(self.getLeftPlayerOf(self.getDealerPID()))
        self.setLastPlayer(self.getDealerPID())
        self.setCurrentTurn(self.getFirstPlayer())
        self.showDialogMessage("Info", "Manual chose.", "Ok" )


    def getValeurCarte(self, carte):
        """ Renvoie la valeur de la carte selon les règles de la belote.

        :param carte (Card):
        :return: (int)
        """

        if(carte.kind == self.atout):
            return self.cartesAtout[carte.value]
        else:
            return self.cartesNAtout[carte.value]

    def nextState(self):
        """  Renvoie le prochain etat du jeu etant donnée une action
            getAction() pour récuperer une action
        """

        # On récupere la phase de jeu actuelle
        phase = self.getCurrentPhase()

        # La distribution des cartes : la première phase
        if( phase == "Start"):
            self.initialPhase()
            return

        # Le choix de l'atout
        if( phase == "Take"):
            self.takePhase()
            return


        if( phase == "initTake2"):
            return
        if( phase == "Take2"):
            self.take2Phase()
            return
        if (phase == "Play"):
            self.playPhase()

            return
        if ( phase == "EndTurn"):
            self.endTurnPhase()
            return

    def isLegalMove(self):
        #TODO: à implémenter
        """
        Renvoie True si l'action est legale dans l'état courant
        :param agent_action:
        :param plugin:
        :return:
        """
        #
        # if(self.getCurrentPhase() == "Play"):
        #     action = self.getAction()
        #     card = action.originSprite
        #     if(card.kind != self.atout):
        #         return False

        return True

class IABelote(IAPlugin):
    def __init__(self):
        IAPlugin.__init__(self, 1)


    def getAction(self, plugin):
        if(plugin.getCurrentPhase() == "Take"):
            return self.choseTrumpPhase(plugin)
        if(plugin.getCurrentPhase() == "Play"):
            return self.playCard(plugin)
        if(plugin.getCurrentPhase() == "Take2"):
            return self.choseTrumpPhase2(plugin)
        return plugin.defAgentAction("none")

    def playCard(self, plugin):
        card = plugin.getCurrentPlayerHand()[0]
        return plugin.defAgentAction("move", card)


    def choseTrumpPhase(self, plugin):
        card = plugin.getCardFromTable(0)
        cardValue = card.value
        if( cardValue >= 13 ):
            return plugin.defAgentAction("move", card)
        else:
            return plugin.defAgentAction("pass")

    def choseTrumpPhase2(self, plugin):
        card = plugin.getCardFromTable(0)
        return plugin.defAgentAction("move", card)


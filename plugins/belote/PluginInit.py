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
        self.setLabeloteFirstPlayer()

        self.appendLogInfoMessage("Chosing trump...")
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

        self.showDialogAction("Info", "Chose a trump or pass", "pass", "pass" )

        if(action.type == "move"):
            card = self.getSelectedCard()
            self.atout = card.kind
            self.dealTrumpCards()
            self.initPlayPhase()
            self.appendLogInfoMessage("Trump has been chosen ")
            self.appendLogInfoMessage(self.kindToStr(self.atout) +
                                      " by player " + str(self.currentTurn()))

        if(action.type == "pass"):
            self.appendLogInfoMessage("Player " + str(self.currentTurn()) + " has passed.")
            if(self.iAmLastPlayerToPlay()):
                self.appendLogInfoMessage("Choosing trump manually...")
                self.initTake2phase()
                return

            self.next_turn()

    def take2Phase(self):
        action = self.getAction()

        self.showDialogAction("Info", "Chose a trump or pass", "pass", "pass2" )


        if(action.type == "move"):
            card = self.getSelectedCard()
            self.atout = card.kind

            self.appendLogInfoMessage("Trump has been chosen ")
            self.appendLogInfoMessage(self.kindToStr(self.atout) +
                                  " by player " + str(self.currentTurn()))
            self.dealTrumpCards()
            self.initPlayPhase()
        if(action.type == "pass2"):
            if(self.iAmLastPlayerToPlay()):
                self.resetTable()
                self.getCurrentPhase("Start")
                self.flushTable()
                #self.showDialogMessage("Info", "Trump has not been chosen restarting.", "Ok" )
                self.appendLogInfoMessage("Trump has not been chosen, restarting" + self.atout)
                return
            self.next_turn()


    def initPlayPhase(self):
         # Le premier joueur à jouer
        self.flushTable()
        self.setLabeloteFirstPlayer()
        self.setCurrentPhase("Play")





    def playPhase(self):
        action = self.getAction()
        if(action.type == "move"):
            self.playSelectedCard()

            if(self.iAmLastPlayerToPlay()):
                self.setCurrentPhase("EndTurn")
                return
            self.next_turn()


    def isWin(self):
        if( self.allHandsEmpty() and
                self.getPlayerScore(0) >
                self.getPlayerScore(1)):
            return True


    def isLost(self):
        if( self.allHandsEmpty() and
                self.getPlayerScore(0) <
                self.getPlayerScore(1)):
            return False

    def endTurnPhase(self):
        totalScore = self.getTableSumCardScore()
        winner = self.getTableBestCardOwner()
        self.laBeloteAddPlayerScore(winner, totalScore)
        self.setFirstPlayer(winner)
        self.setLastPlayer(self.getRightPlayerOf(winner))
        self.setCurrentTurn(winner)
        self.setCurrentPhase("Play")
        #self.showDialogMessage("Info", "Hand winner is " + str(winner), "Ok" )
        self.appendLogInfoMessage("Hand winner is " + str(winner) + " with score :" + str(totalScore))
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
        self.setLabeloteFirstPlayer()


    def laBeloteAddPlayerScore(self, pid, score):
        if(pid == 0 or pid == 2):
            self.addPlayerScore(0,score)
        else:
            self.addPlayerScore(1,score)

    def setLabeloteFirstPlayer(self):
        self.setFirstPlayer(self.getLeftPlayerOf(self.getDealerPID()))
        self.setLastPlayer(self.getDealerPID())
        self.setCurrentTurn(self.getFirstPlayer())

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
        """
        Renvoie True si l'action est legale dans l'état courant
        :param agent_action:
        :param plugin:
        :return:
        """

        if(self.getCurrentPhase() == "Play"):
            if(len(self.getTable()) > 0):
                action = self.getAction()
                if(action.type == "move"):
                    hand = self.getCurrentPlayerHand()

                    turnKind =  self.getCardFromTable(0).kind
                    selectedCard=action.originSprite

                    kind = selectedCard.kind

                    if(kind != turnKind):
                        if( self.currentHandGotKind(turnKind) ):
                            return False

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
        if( plugin.getFirstPlayer() == plugin.currentTurn()):
            card = plugin.getHandBestCard()
        else:
            turnKind = plugin.getCardFromTable(0).kind
            if( plugin.currentHandGotKind(turnKind)):
                card = plugin.getHandBestCard(turnKind)
            else:
                card = plugin.getHandBestCard()
        return plugin.defAgentAction("move", card)


    def choseTrumpPhase(self, plugin):
        card = plugin.getCardFromTable(0)
        cardValue = card.value
        if( cardValue == 11 ):
            return plugin.defAgentAction("move", card)
        else:
            return plugin.defAgentAction("pass")

    def choseTrumpPhase2(self, plugin):
        card = plugin.getCardFromTable(0)
        return plugin.defAgentAction("move", card)


""" Autheur Giuseppe Federico
"""

from game.Plugin import Plugin, IAPlugin

class PluginInit(Plugin):
    """ Plugin pour 'La Bataille'
    """

    def __init__(self):
        Plugin.__init__(self, "La Bataille")

        # Atout courant
        self.atout=None

        # Définition des valeurs des cartes atout
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

        # Définition des valeurs des cartes non atout
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

        """

        # Initialisation des joueurs
        self.initPlayers(4)

        # Ajout l'IA des opposants
        self.opponents.append(IABelote())

    def initialPhase(self):
        """ La phase initiale de la belote.

        """

        # Enlève les cartes qui sont pas utilisées
        self.removeRangeOfCards(self.getTableDeck(), 2,6, ['h','c','s','d'] )

        # On choisit un donneur au hazard
        self.choseRandomDealer()

        # Choisir le premier et le dernier joueur par rapport
        # au dealer
        self.setFirstAndLastPlayers(self.getLeftPlayerOf(
            self.getDealerPID()))

        # Les joueurs reçoivent chacun 5 cartes.
        self.dealCards(5)

        # Une carte est placée, face découverte, au milieu de la table de jeu.
        self.dealToTable(1)

        # On affiche des messages d'infos
        self.appendLogInfoMessage("Choix de l'atout.")

        # Changement de phase
        self.setCurrentPhase("Take")


    def dealRestCards(self):
        # Distribution du reste des cartes
        for i in range(self.getnbPlayers()):
            if (i != self.currentTurn()):
                self.dealTo(i, 3)
            else:
                self.dealTo(i, 2)
                card = self.popCardFromTable()
                self.appendCardToMyHand(card)

    def takePhase(self):
        """ Premiere phase de choix de l'atout.
        """
        action = self.getAction()

        # Affiche choix de l'action
        self.showDialogAction("Info", "Selectionner l'atout ou passer", "Passer.", "pass" )

        # L'atout a été séléctionné
        if(action.type == "move"):
            self.choisirAtout()


        # Le joueur a passé
        if(action.type == "pass"):
            self.appendLogInfoMessage("Player " + str(self.currentTurn()) + " has passed.")

            # Si on est le dernier à jouer
            if(self.iAmLastPlayerToPlay()):
                self.appendLogInfoMessage("Choix de l'atout, 2ème phase")
                self.initTake2phase()
                return

            self.next_turn()

    def initTake2phase(self):
        """ Initialisation de la 2ème phase de choix de l'atout
        :return:
        """

        # Si l'on selectionne une des ces cartes
        # on selectionne le type associé comme atout
        h = self.defCard(1,'h')
        s = self.defCard(1,'s')
        c = self.defCard(1,'c')
        d = self.defCard(1,'d')
        h.owner = 0
        s.owner = 1
        c.owner = 2
        d.owner = 3
        self.appendCardToTable(h)
        self.appendCardToTable(s)
        self.appendCardToTable(c)
        self.appendCardToTable(d)


        self.setCurrentPhase("Take2")
        self.setLabeloteFirstPlayer()


    def choisirAtout(self):
        """ Mémoriser l'atout et afficher des messages d'infos
        """
        card = self.getSelectedCard()

        # Mémorise l'atout choisi
        self.atout = card.kind

        # Distribution du reste des cartes
        self.dealRestCards()

        self.initPlayPhase()

        # Affiche les message d'infos
        self.showBlockingDialogMessage(self.kindToStr(self.atout) +
                                  " has been chosen by player " + str(self.currentTurn()) + "as Trump.")
        self.appendLogInfoMessage(self.kindToStr(self.atout) +" has been chosen ")
        self.appendLogInfoMessage("by player " + str(self.currentTurn()))

    def take2Phase(self):
        """ 2ème phase de choix de l'atout

        """
        action = self.getAction()

        self.showDialogAction("Info", "Chose a trump or pass.", "pass", "pass2" )

        if(action.type == "move"):
            self.choisirAtout()
        if(action.type == "pass2"):
            if(self.iAmLastPlayerToPlay()):
                self.resetTable()
                self.getCurrentPhase("Start")
                self.appendLogInfoMessage("Trump has not been chosen, restarting" + self.atout)
                return
            self.next_turn()


    def initPlayPhase(self):
        """ Initialisation de la phase de jeu
        """
         # Le premier joueur à jouer
        self.flushTable()
        self.setLabeloteFirstPlayer()
        self.setCurrentPhase("Play")


    def playPhase(self):
        """ Phase de jeu
        """

        if(self.currentTurn() == self.getFirstPlayer()):
            self.flushTable()

        action = self.getAction()
        if(action.type == "move"):
            self.playSelectedCard()

            if(self.iAmLastPlayerToPlay()):
                self.setCurrentPhase("EndTurn")
                return
            self.next_turn()


    def isWin(self):
        """ On vérifie la condition de victoire
        """
        if( self.allHandsEmpty() and
                self.getPlayerScore(0) >
                self.getPlayerScore(1)):
            return True


    def isLost(self):
        """ On vérifie la condition de perte
        """
        if( self.allHandsEmpty() and
                self.getPlayerScore(0) <
                self.getPlayerScore(1)):
            return False

    def endTurnPhase(self):
        """ Fin du tour, on calcule et affecte le score
        """
        totalScore = self.getTableSumCardScore()
        winner = self.getTableBestCardOwner()
        self.laBeloteAddPlayerScore(winner, totalScore)
        self.setFirstPlayer(winner)
        self.setLastPlayer(self.getRightPlayerOf(winner))
        self.setCurrentTurn(winner)
        self.setCurrentPhase("Play")

         # Affiche les message d'infos
        self.showBlockingDialogMessage("Hand winner is " + str(winner) + " with score :" + str(totalScore))
        self.appendLogInfoMessage("Hand winner is " + str(winner) + " with score :" + str(totalScore))


    def laBeloteAddPlayerScore(self, pid, score):
        """ On affecte le score à la team et non au joueur ( comportement par défaut)
        """
        if(pid == 0 or pid == 2):
            self.addPlayerScore(0,score)
        else:
            self.addPlayerScore(1,score)

    def setLabeloteFirstPlayer(self):
        """ Le premier joueur est celui à la gauche du donneur
        """
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
        action = self.getAction()



        if(self.getCurrentPhase() == "Play"):
            if(len(self.getTable()) > 0):
                if( action.originDrawable == -1 ):
                    return False

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
    """ Un opposant
    """

    def __init__(self):
        IAPlugin.__init__(self, 1)


    def getAction(self, plugin):
        """ On reçoit une action en fonction de la phase de jeu
        """
        if(plugin.getCurrentPhase() == "Take"):
            return self.choseTrumpPhase(plugin)

        if(plugin.getCurrentPhase() == "Play"):
            return self.playCard(plugin)

        if(plugin.getCurrentPhase() == "Take2"):
            return self.choseTrumpPhase2(plugin)

        return plugin.defAgentAction("none")

    def playCard(self, plugin):
        """ Joue une carte avec des algorithmes simples.
        """
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
        """ Choix de l'atout avec des conditions simples.
        """
        card = plugin.getCardFromTable(0)
        cardValue = card.value
        if( cardValue == 11 ):
            return plugin.defAgentAction("move", card)
        else:
            return plugin.defAgentAction("pass")

    def choseTrumpPhase2(self, plugin):
        """ Choix de l'atout dans la 2éme phase avec des conditions simples.
        """
        hand = plugin.getCurrentPlayerHand()
        if( plugin.handHasCardValue(11)):
            card = plugin.getHandCard(11)
            if(card.kind == 'h'):
                trump = plugin.getCardFromTable(1)
                return plugin.defAgentAction("move", trump)
            if(card.kind == 's'):
                trump = plugin.getCardFromTable(2)
                return plugin.defAgentAction("move", trump)
            if(card.kind == 'c'):
                trump = plugin.getCardFromTable(3)
                return plugin.defAgentAction("move", trump)
            if(card.kind == 'd'):
                trump = plugin.getCardFromTable(4)
                return plugin.defAgentAction("move", trump)
        else:
            return plugin.defAgentAction("pass2")


# -*- coding: utf-8 -*-

from random import randint
from environment.Card import Card
from environment.CardStack import CardStack
from environment.DeckGenerator import DeckGenerator
from environment.Dialog import Dialog
from environment.Table import Table
from game.agents.AgentAction import AgentAction
from game.agents.Player import Player


class PluginManager:
    """ La classe pluginManager fais office de couche d'abstraction entre le moteur de jeu et le plugin.
        On y retrouve toutes les fonctions utiles pour définir les réglés du jeu à l’intérieur du plugin.
    """


    def __init__(self, name):
        self.TABLE_PID = -1
        self.PLAYER_PID = 0
        self.opponents = []

        # Initialisation du jeu
        self.initState = InitState()
        self.gameState = None
        self.agentAction = None

        # L'id de la phase courante
        self.phase = "Start"

        # Plugin name
        self.name = name


    ################ Déclaration des phases de jeu ####################

    def getCurrentPhase(self):
        """ Retourne la phase de jeu courante.

        :return (String):
        """
        return self.phase

    def setCurrentPhase(self, phaseName):
        """ Affecte la phase de jeu courante.

        :return: None
        """
        self.phase = phaseName

    ###################################################################

    def nextState(self, gameState, agent_action):
        """ Fonction nextState abstraite à implémenter dans le plugin.
        :return:
        """
        return None

    def pluginInit(self):
        """ Fonction init abstraite à implémenter dans le plugin.
        :return:
        """

        return None

    def initGameState(self):
        """ Initialise le jeu de cartes et appele la fonction
            pluginInit redéfinie dans le plugin.

        :return: InitState
        """

        deck = self.initState.generateShuffledDeck()
        self.initState.setTableDeck(deck)

        # Appel à la fonction pluginInit()  redéfinie dans le plugin
        self.pluginInit()

        return self.initState

    def initPlayers(self, nbPlayers):
        """ Initialise le numero de joueurs.

        :param nbPlayers (int) : Le numero de joueurs
        :return: None
        """
        self.initState.initPlayers(nbPlayers)


    def GNextState(self, gameState, agent_action):
        """ Cette fonction apelle la fonction nextState du plugin
            actuel.

        :param gameState (GameState): game state courant
        :param agent_action ( AgentAction): Action courante
        :return: Le nextState calculé par le plugin
        """

        self.agentAction = agent_action

        if (  self.agentAction == None ):
            self.agentAction = self.defAgentAction("none")

        if ( not self.isLost() and not self.isWin()):
            if (self.currentTurn() == 0):
                self.hideDialogMessage()

            self.nextState()
            self.sortAllHandsByValue()

        else:
            if (self.isWin()):
                self.showBlockingDialogMessage("Victoire", "Vous avez gangé.", "Ok")
            else:
                self.showBlockingDialogMessage("Perdu", "Vous avez perdu.", "Ok")
        return self.gameState

    def GisLegalMove(self, gameState, agent_action):
        """
        Dans cette fonction on va vérifier si l'action
        passé en paramètre est une action valide.

        :param gameState: GameState
        :param agent_action: AgentAction
        :return: boolean
        """

        self.gameState = gameState
        self.agentAction = agent_action
        if (self.agentAction == None or self.agentAction.type == "None"):
            return True
        else:
            return self.isLegalMove()

    def lose(self):
        """ True si la partie est perdue, false sinon.
        :return:
        """
        self.gameState.lose = True

    def getAction(self):
        """
        Récupere la dernière action d'un joueur.
        :return:
        """

        return self.agentAction


    def getTable(self):
        """
        Cette fonction renvoie la table de jeu
        :return: CardStack
        """
        return self.gameState.table

    ###################### HUD #################################

    def showBlockingDialogMessage(self, message, title="Info", buttonText="Ok"):
        """ Affiche un dialog message qui met le jeu en pause.
        :param message: Le message
        :param title: Le titre
        :param buttonText: le texte du bouton
        :return: None
        """

        self.gameState.paused = True
        if (not self.gameState.dialog.visible):
            self.gameState.dialog.popDialog(title, message, buttonText, "unPause")

    def showDialogAction(self, title, message, buttonText, action):
        """Affiche un dialog message enregistre une action.
        """

        if (self.isPlayerTurn() and self.agentAction.type == "none"):
            self.gameState.dialog.popDialog(title, message, buttonText, action)


    def hideDialogMessage(self):
        """
        Cache le dernier dialog message.
        :return:
        """
        if (self.gameState.dialog.visible):
            self.gameState.dialog.hideDialog()

    def appendLogInfoMessage(self, message):
        """
        Ajoute un message au log en bas à droite.
        :param message: texte du message à afficher
        :return:
        """
        self.gameState.infoLog.append(message)


    def initDialog(self, title, msg, tbutton):
        """
        Initialise le dialog.

        """
        self.initState.initDialog(title, msg, tbutton)

    ############################################################


    ########################## Fonctions de Jeu ###############################

    def pause(self):
        """ Met le jeu en pause.
        """

        self.gameState.paused = True

    def unPause(self):
        """ Remet le jeu en éxécution.
        """

        self.gameState.paused = False


    def restartGame(self):
        """ Réinitialise le jeu.
        :return:
        """
        self.gameState.restart(self.initGameState())

    def playSelectedCard(self):
        """ Joue la carte selectionné.
        :return:
        """

        action = self.getAction()
        card = action.originSprite
        if ( card.hidden ):
            card.flipCard()
        self.playCard(action.originSprite)

    def getCurrentPlayerFirstCard(self):
        """ Retourne la première carte de la main du joueur courant si elle
        existe.

        :return (Card): Une Carte ou None
        """

        currentHand = self.getCurrentPlayerHand()

        if ( len(currentHand) <= 0 ):
            raise PluginException("The number of players must be greater than 0.")

        return currentHand[0]

    def getCurrentPlayerPID(self):
        """ Renvoie le PID du joueur courant.
        :return:
        """
        return self.currentTurn()

    ###########################################################################

    ######################### Table Functions ##################################

    def getLastCards(self, nb):
        """ Renvoie un tableu avec les nb dérnières cartes.

        :param nb (int):
        :return: CardStack
        """
        table = self.getTable()

        return table[len(table) - nb:len(table)]

    def getNbTableCards(self):
        """ Renvoie le nombre de cartes sur la table.

        :return (int):
        """

        return len(self.getTable())

    def appendCardToTable(self, card):
        """
        Ajoute la carte card à la table.

        :param card (Card):
        :return: None
        """

        self.getTable().append(card)

    def popCardFromTable(self, ind=0):
        """ Prend la carte d'index ind de la table.

        :param index (int): ( default 0)
        :return: (Card)
        """

        if ( not self.getTable() ):
            raise PluginException("Cannot pop, empty table.")

        return self.getTable().pop(0)

    def getCardFromTable(self, index):
        """ Récupère la carte 'index' de la talbe
        :param (int) index: L'index de la table
        :return:
        """
        if (len(self.getTable()) <= 0):
            raise PluginException("Table is empty")
        return self.getTable()[index]

    def resetTable(self):
        """ Fonction qui reset la table.

        :return: None
        """
        # Reinit Deck
        deck = self.initState.generateShuffledDeck()
        self.gameState.table.deck = deck

        # Reinit Table
        for i in range(self.getnbPlayers()):
            self.getPlayer(i).hand = CardStack()

        self.flushTable()

    ######################### /Table Functions #################################

    #########################        Actions          ##########################

    def getSelectedCard(self):
        """ Renvoie la carte selectionné
        :return: (Card)
        """

        sprite = self.getAction().originSprite
        if ( not isinstance(sprite, Card) ):
            raise PluginException("I can select only cards.")
        else:
            return sprite

    #########################        /Actions          ##########################

    ######################## Cards Functions            #########################
    def defCard(self, value, kind):
        """ Définit une carte manuellement
        :param value: la valeur de la carte
        :param kind: le type de la carte
        :return:
        """
        return Card(value, None, kind)

    ######################## /Cards Functions            #########################
    ######################### Deck Functions ##################################
    def isDeckEmpty(self):
        """ Renvoie false si le jeu de cartes est non vide, true sinon
        :return:
        """
        return not len(self.getTableDeck())

    def removeRangeOfCards(self, cardStack, inf=0, sup=13, kinds=[]):
        """ Supprime les cartes de 'cardStack' qui ont une valeur comprise entre
        [inf, sup] et qui font partie de un des types de la liste 'kind' parmi
        h, c, s et d.

        :param inf (int): borne inferieure (comprise) (default = 13).
        :param sup (int): borne superieure (comprise) (default = 0).
        :param cardStack (CardStack):
        :param kind (list of String): une liste de types parmi h, c, s et d.
        :return: Un CardStack modifié.
        """

        if ( cardStack.isEmpty()):
            raise PluginException("CardStack is empty, cannot remove cards.")

        toRemove = []
        for card in cardStack:
            if ( card.value <= sup and
                         card.value >= inf):
                for kind in kinds:
                    if ( card.kind == kind):
                        toRemove.append(card)

        for card in toRemove:
            cardStack.remove(card)

        return cardStack

    ######################### /Deck Functions ##################################

    ######################## Hand Functions ##################################
    def sortAllHandsByValue(self):
        """ Trie tous les main par valeur en ordre croissant.
        :return:
        """
        for pid in range(self.getnbPlayers()):
            self.sortHandByValue(pid)

    def sortHandByValue(self, pid):
        """ Trie la main de 'pid' par valeur en ordre croissant.
        """
        hand = self.getPlayerHand(pid)

        valueList = []

        i = 0
        # Ajout des cartes avec position initiale
        for card in hand:
            valueList.append((i, self.getValeurCarte(card)))
            i += 1

        valueListSorted = sorted(valueList, key=lambda tup: tup[1])

        resu = []
        for value in valueListSorted:
            posInit = value[0]
            card = hand[posInit]
            resu.append(card)

        self.getPlayer(pid).hand = resu


    def appendCardToHand(self, pid, card):
        """ Ajoute card à la main du joueur pid.

        :param pid (int):
        :param card( Card):
        :return:
        """
        if ( pid != 0 ):
            card.flipCard()

        # Change le propriétaire
        card.owner = pid

        self.getPlayerHand(pid).append(card)

    def appendCardToMyHand(self, card):
        """ Ajoute card à la main du joueur courant

        :param pid (int):
        :param card( Card):
        :return:
        """

        self.appendCardToHand(self.currentTurn(), card)

    def isPlayerHandEmpty(self, pid):
        """ True si la main du joueur pid est vide, false sinon
        :param pid:
        :return:
        """
        return not self.getPlayerHand(pid)

    def allHandsEmpty(self):
        """ Renvoie true si tous les main des adversaires sont vides, false sinon

        :return (boolean):
        """

        for pid in range(self.getnbPlayers()):
            if ( not self.isPlayerHandEmpty(pid) ):
                return False

        return True


    def getHandBestCard(self, kind=None):
        """ Renvoie la meilleure carte en main.
            Si kind est specifié, renvoie la meilleure carte d'un type en particulier

        :return (Card):
        """
        hand = self.getCurrentPlayerHand()

        if ( len(hand) <= 0 ):
            raise PluginException("Hand is empty!")
        firstCard = hand[0]
        first = True
        resu = None

        if (kind != None):
            for card in hand:
                if ( card.kind == kind):
                    if (first):
                        max = self.getValeurCarte(card)
                        resu = card

                    elif ( card.kind == kind and self.getValeurCarte(card) > max):
                        max = self.getValeurCarte(card)
                        resu = card
        else:
            for card in hand:

                if (first):
                    max = self.getValeurCarte(card)
                    resu = card

                elif (  self.getValeurCarte(card) > max):
                    max = self.getValeurCarte(card)
                    resu = card

        return resu

    def handGotKind(self, pid, kind):
        """ Cette fonction renvoie true si la main du joueur 'pid' contient

        une carte de type 'kind'.

        :param pid (int):
        :param kind (String):
        :return: ( boolean )
        """

        hand = self.getPlayerHand(pid)

        if ( not hand ):
            raise PluginException("Hand is empty.")

        for card in hand:
            if ( card.kind == kind):
                return True

        return False

    def currentHandGotKind(self, kind):
        """ Renvoie true si la main du joueur courant contient une carte du type

        'kind', false sinon.

        :param kind (String):
        :return:
        """

        return self.handGotKind(self.currentTurn(), kind)

    def handHasCardValue(self, cardValue):
        """ Renvoie true si la main du joueur courant contient la carte

        de valeur 'cardValue', false sinon,

        :param cardValue( int ):
        :return:
        """

        hand = self.getCurrentPlayerHand()

        for card in hand:
            if ( card.value == cardValue):
                return True
        return False

    def getHandCard(self, value, kind=None):
        """ Renvoie la carte de valeur 'value' ( de type kind si spécifié,
         une au hazard sinon )

        :param value (int):
        :param kind (String):
        :return: (Card)
        """
        if ( not self.handHasCardValue(value)):
            raise PluginException("The hand does not contains the card requested")

        hand = self.getCurrentPlayerHand()
        if (kind == None):
            for card in hand:
                if (card.value == value):
                    return card
        else:
            for card in hand:
                if (card.value == value and card.kind == kind):
                    return card
        return None

    ######################## /Hand Functions ##################################
    def getTable(self):
        """
        Cette fonction renvoie les cartes de la table
        :return: CardStack
        """
        return self.gameState.table.table


    def getCurrentPlayer(self):
        """ Renvoie le joueur courant
        :return:
        """
        return self.gameState.getPlayer(self.currentTurn())


    def pid(self, object):
        """ Renvoie le pid d'un objet
        :param object:
        :return: (int) pid
        """
        if ( hasattr(object, "getPid()") ):
            return object.getPid()

        else:
            print(object + " ne contient pas un pid.")


    def getPlayerHand(self, pid):
        """
        Cette fonction renvoie ma main du joueur à partir d'un pid
        :param pid: int
        :return: CardStack
        """
        if (pid == -1 ): return self.gameState.table.table
        return self.gameState.table.getPlayerHand(pid)

    def getCurrentPlayerDeck(self):
        """ Renvoie le jeu de cartes du joueur
        :return (int):
        """

        return self.gameState.table.players[self.currentTurn()].deck

    def getTableDeck(self):
        """ Retour le jeu de cartes principal
        :return:
        """

        return self.gameState.table.deck

    def win(self):
        """ La partie est gangé
        :return:
        """
        self.gameState.win = True


    def currentTurn(self):
        """
        Renvoie le tour courrant
        :return:
        """
        return self.gameState.turn

    def getnbPlayers(self):
        return self.gameState.table.nbPlayers


    def pickCardFrom(self, pid):
        """Déplace une carte du jeu de carte  pid à sa main

        :param pid (int): Le pid du joueur résponsable de l'action
        :return:
        """
        if (pid != -1):
            card = self.gameState.getPlayer(pid).deck.pop()
        else:
            card = self.gameState.table.deck.pop()

        self.appendCardToMyHand(card)


    def isPlayerTurn(self):
        return (self.gameState.turn == 0)

    def flushTable(self):
        """ Efface le contenu de la table
        """

        self.gameState.table.flush()

    def playCard(self, card):
        """ Joue la carte 'card'

        :param int card:
        :return:
        """

        oc = card
        od = self.currentTurn()
        dd = self.TABLE_PID

        self.gameState.moveCard(oc, od, dd)

    def isLost(self):
        """ Renvoie true si la partie est perdue, false sinon
        :return:
        """
        return self.gameState.lose

    def isWin(self):
        """ Renvoie true si la partie est gagné, false sinon
         :return:
        """
        return self.gameState.win

    def getCurrentPlayerHand(self):
        """ Retourne la main du joueur courant

        :return: un CardStack
        """
        return self.gameState.getPlayerHand(self.currentTurn())

    def getPlayer(self, pid):
        """ Retourne un le PlayerState du joueur (pid)

        :param pid (int): Le pid du joueur que l'on veut obtenir
        :return: un PlayerState
        """
        return self.gameState.table.players[pid]

    def getValeurCarte(self, carte):
        """ Renvoie la valeur de la carte selon les régles du jeu.

        :param carte (Card):
        :return: (int)
        """

        return self.gameState.cardValues[carte.value]

    def getAction(self):
        """ récoupère l'action courante

        :return:
        """
        if (self.agentAction == None):
            return self.defAgentAction("none")
        return self.agentAction

    def next_turn(self):
        """ Fonction qui passe le tourne
        """
        nb = self.gameState.getnbPlayers()
        tmp = (self.gameState.turn + 1)
        resu = tmp % nb
        self.gameState.turn = resu

    ############################### Dealing functions ##########################

    def choseRandomDealer(self):
        """ Fonction qui choisi un dealer au hazard.
        :return: None
        """

        self.setDealer(randint(0, self.getnbPlayers() - 1))

    def setDealer(self, pid):
        """ Designe le distributeur des cartes (pid).
        :param pid (int):
        :return: None.
        """

        for i in range(self.getnbPlayers()):
            if ( i != pid):
                self.getPlayer(i).dealer = False
            else:
                self.getPlayer(pid).dealer = True

    def getDealerPID(self):
        """ Retourne le pid du distributeur des cartes.

        :return (int): -1 si le dealer n'est pas defini.
        """

        for i in range(self.getnbPlayers()):
            if (self.getPlayer(i).dealer):
                return i
        raise PluginException("No dealer defined")

        return -1

    def dealToTable(self, nbCards):
        """ Déplace nbCards cartes du jeu de carte principale à la table
        :return: None
        """

        for i in range(nbCards):
            card = self.getTableDeck().pop()
            self.appendCardToTable(card)

    def dealTo(self, pid, nbCards):
        """ Ditribue nbCards au joueur (pid)
        :param pid (int):
        :param nbCards (int):
        :return: None
        """

        for i in range(nbCards):
            if ( self.isDeckEmpty()):
                raise PluginException("Cannot pick, deck is empty")
            card = self.getTableDeck().pop()

            self.appendCardToHand(pid, card)

    def dealCards(self, nb_cards):
        """ Distribution de nb_cards en sens antihoraire
        :param nb_cards:
        :param deck_pid:
        """

        deck = self.gameState.table.deck

        for pid in range(self.gameState.getnbPlayers()):
            self.dealTo(pid, nb_cards)

    ############################## Dealing functions ##########################

    ###################### Score Functions #####################
    def getPlayerScore(self, pid):
        """ Le score du joueur de pid 'pid'

        :param (int) pid:
        :return:
        """
        return self.getPlayer(pid).score

    def hasBestScore(self, pid):
        """ Renvoie true si 'pid' a le meilleure score, false sinon.
        :param pid:
        :return:
        """
        resu = True
        ps = self.getPlayerScore(pid)
        for i in range(self.getnbPlayers()):
            if (ps < self.getPlayerScore(i)):
                resu = False
        return resu

    def IHaveBestScore(self):
        """ Renvoi true si le joueur courant a le meilleur score, false sinon.
        :return: boolean
        """
        return self.hasBestScore(self.getCurrentPlayerPID())

    def getCurrentPlayerScore(self):
        """ Renvoie le score du joueur
        :return (int):
        """

        return self.gameState.getCurrentPlayer().score

    def getTableCardsPoints(self, inf=0, sup=None):
        """ Affecte au score du joueur courant la somme des valeurs des
        cartes d'index [inf, sup] ( toutes les cartes de la table si pas
        de paramètres.

        :param inf (int):
        :param sup (int):
        :return: None
        """
        if ( sup == None):
            sup = self.getNbTableCards()
        sum = self.getTableSumCardScore(inf, sup)
        self.addPlayerScore(self.getCurrentPlayerPID(), sum)


    def getCardsPoints(self, pid, cards):
        """ Affecte au joueur pid la valeur de la liste des cartes
        passées en argument
        :param (int):
        :param List:
        :return:
        """
        for card in cards:
            self.addPlayerScore(pid,
                                self.getValeurCarte(card))

    def getCardsValueSum(self, cards):
        """ Renvoie la somme de la valeur cartes dans la liste
        :param cards (list):
        :return:
        """
        resu = 0

        for card in cards:
            resu += self.getValeurCarte(card)

        return resu

    def getTableSumCardScore(self, inf=0, sup=None):
        """ Renvoie la somme des valeurs des cartes sur la table.
            On peux spécifier les indexes.

        :return (int):
        """
        if ( sup == None):
            sup = self.getNbTableCards()
        resu = 0

        for i in range(inf, sup):
            resu += self.getValeurCarte(self.getTable()[i])

        return resu

    def getTableBestCardOwner(self):
        """ Retourne le pid du joueur avec la carte de valeur plus haute
            présent sur la table.

            :return: pid (int):
        """

        table = self.getTable()
        if ( len(table) <= 0 ):
            raise PluginException("Table is empty!")
        firstCard = table[0]
        max = self.getValeurCarte(firstCard)
        pid = firstCard.owner

        for card in self.getTable():
            if ( self.getValeurCarte(card) > max):
                max = self.getValeurCarte(card)
                pid = card.owner

        return pid


    def addPlayerScore(self, pid, score):
        """ Ajoute le score 'score' au joueur 'pid'
        :param (int) pid:
        :param (int) score:
        :return: None
        """
        self.getPlayer(pid).score += score

    ###################### /Score Functions #####################

    ###################### Turn Functions #######################
    def getFirstPlayer(self):
        """ Renvoie le pid du premier joueur à jouer

        :return:
        """
        for i in range(self.getnbPlayers()):
            if (self.getPlayer(i).first):
                return i
        raise PluginException("No first player defined")

        return -1

    def setFirstAndLastPlayers(self, first, last=None):
        """ Affecte le premier et le dernier joueur.

            Le dernier joueur est celui à  droite de 'first' si
            'last' n'est pas spécifié, 'last' sinon.

            :param first (int): pid
            :param last (int): pid (default) None
        """

        nbp = self.getnbPlayers()

        if ( first >= nbp or first < 0):
            raise PluginException("First pid out of range ")

        self.setFirstPlayer(first)

        if (last):
            if ( last >= nbp or last < 0):
                raise PluginException("Last pid out of range ")
            self.setLastPlayer(last)
        else:
            self.setLastPlayer(self.getRightPlayerOf(first))

    def isPlayerTurn(self):
        """ True si c'est le tour du joueur
        :return: None
        """
        return (self.currentTurn() == 0)

    def getTurnTableKind(self):
        """ Renvoie le type de tour courant

        :return (String):
        """
        return self.getCardFromTable(0).kind

    def setFirstPlayer(self, pid):
        """ Affecte le premier joueur au jouer pid
        :param pid:
        :return:
        """

        for i in range(self.getnbPlayers()):
            if (i == pid):
                self.getPlayer(i).first = True
            else:
                self.getPlayer(i).first = False

    def iAmLastPlayerToPlay(self):
        """ Renvoie true si le joueur courant est le dérnier joueur du tour.
        :return:
        """
        return self.getPlayer(self.currentTurn()).last

    def setLastPlayer(self, pid):
        """ Affecte le dernier joueur au joueur pid
        :param pid:
        :return:
        """

        for i in range(self.getnbPlayers()):
            if (i == pid):
                self.getPlayer(i).last = True
            else:
                self.getPlayer(i).last = False

    def setCurrentTurn(self, turn):
        """ Change current turn

        :param turn (int):
        :return: None
        """
        self.gameState.turn = turn

    def getLeftPlayerOf(self, pid):
        """ Renvoie le pid du joueur à la gauche de pid
        :param pid (int):
        :return:
        """
        return ((pid + 1) % self.getnbPlayers())

    def getRightPlayerOf(self, pid):
        """ Renvoie le pid du joueur à la droite de pid
        :param pid (int):
        :return:
        """
        return ((pid - 1) % self.getnbPlayers())

    ###################### /Turn Functions #######################

    ###################### Utils #################################

    def kindToStr(self, kind):
        """ Traduit un type de carte en String,
        :param kind:
        :return:
        """
        kinds = {
            's': "Piques",
            'h': "Coeurs",
            'd': "Carrés",
            'c': "Trèfles"

        }

        return kinds.get(kind)

        ##############################################################

    ######################      IA      ########################

    def defAgentAction(self, type,
                       originSprite=None, originDrawable=None):
        """ Cette fonction définit une action de l'opposant.

        :param type (String): Le type de l'action.
        :param originSprite (ClickableSprite): Un sprite d'origine.
        :param originDrawable (Drawable): Un drawable.
        :return: (Action): Une action.
        """

        action = AgentAction(type)
        action.originSprite = originSprite
        action.originDrawable = originDrawable

        return action

    ######################      /IA      #######################
    def setCardValues(self, cardValues):
        """
         Set the value of every card
        :param cardValues:
        :return:
        """
        self.gameState.cardValues = cardValues


class IAPlugin(Player):
    def __init__(self, id):
        Player.__init__(self, id)

    def getAction(self, plugin):
        """ Reçois l'action de l'adversaire, à implémenter dans le plugin.
        """
        return None

    def PgetAction(self, agent_state, plugin, event=None):
        return self.getAction(plugin)


################################### Init State ###################################

class InitState:
    """ Fonctions pour l'initialisation du jeu.
    """

    def __init__(self):
        self.turn = 0
        self.table = Table()
        self.win = False
        self.dialog = Dialog()

        self.cardValues = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 10,
            11: 11,
            12: 12,
            13: 13,
            14: 14
        }


    def initPlayers(self, nbPlayers):
        """
        Initialise le nombre de joueurs
        :param (int) nbPlayers:
        """
        if ( nbPlayers <= 0 ):
            raise PluginException("The number of players must be greater than 0.")
        for i in range(0, nbPlayers):
            self.addPlayerState(CardStack(), CardStack())

    def initDialog(self, title, msg, tbutton):
        """ Initialise le dialog
        """
        self.dialog.popDialog(title, msg, tbutton)


    def addPlayerState(self, hand=CardStack(), deck=CardStack()):
        """ Ajoute un joueur au jeu
        :param hand: CardStack() la main initiale
        :param deck: CardStack() le jeu initial
        :return:
        """

        self.table.addPlayer(hand, deck)

    def generateShuffledDeck(self):
        """ Générer un jeu de cartes mélangé.

        :return: (CardStack)
        """

        deck = DeckGenerator.deckFactory()
        deck.shuffle()
        return deck

    def setFirstPlayer(self, pid):
        """ Initialise le premier joueur à  jouer.
        """
        self.turn = pid

    def setCardValues(self, vals):
        """ Initialise le tableau des valeurs des cartes

        """
        self.cardValues = vals

    def setTableDeck(self, deck):
        """ Initialise le jeu de cartes de la table
        :param deck (CartStack):
        :return:
        """
        self.table.deck = deck


class PluginException(Exception):
    """ Une exception du plugin
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
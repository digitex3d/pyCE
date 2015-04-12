""" Autheur Giuseppe Federico 
"""
from environment.CardStack import CardStack
from environment.DeckGenerator import DeckGenerator
from environment.Dialog import Dialog
from environment.Table import Table
from game.agents.AgentAction import AgentAction
from game.agents.Player import Player

class PluginException(Exception):
    """ Une exception du plugin
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class Plugin:
    """ Cette classe représente un Plugin 
    """


    def __init__(self, name):
        test = True
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

    def setCurrentPhase(self,  phaseName):
        """ Affecte la phase de jeu courante.

        :return: None
        """
        self.phase = phaseName

    ###################################################################

    def nextState(self, gameState, agent_action):
        """ Classe abstraite à implémenter dans le plugin.
        :return:
        """
        return None

    def pluginInit(self):
        """ Classe abstraite à implémenter dans le plugin.
        :return:
        """
        return None

    def initGameState(self):
        deck = self.initState.generateShuffledDeck()
        self.initState.setTableDeck(deck)
        self.pluginInit()
        return self.initState

    def initPlayers(self, nbPlayers):
        """ Initialise le numero de joueurs
        :param nbPlayers (int) : Le numero de joueurs
        :return: None
        """
        self.initState.initPlayers(nbPlayers)


    def GNextState(self, gameState, agent_action):
        """ Cette fonction fait une copie de l'état de jeu , affecte le gamestate et
            l'action au plugin puis apelle la fonction nextState du plugin.
            actuel au plugin.

        :param gameState (GameState): game state courant
        :param agent_action: Action courante
        :return: Le nextState calculé par le plugin
        """
        self.agentAction = agent_action


        if(  self.agentAction.type == "None" ):
            return self.gameState
        else:
            if( not self.isLost() and not self.isWin()):
                if(  self.agentAction.type == "dialog" ):
                    self.gameState.dialog.hideDialog()
                self.nextState()
        return self.gameState

    def GisLegalMove(self, gameState, agent_action):
        new_state = gameState.copy()
        self.gameState = new_state
        self.agentAction = agent_action
        return self.isLegalMove()

    def lose(self):
        """ La partie est perdue
        :return:
        """
        self.gameState.lose = True

    def getAction(self):
        return self.agentAction

    def lastPlayerToPlay(self):
        if( self.currentTurn() == self.getnbPlayers()-1):
            return True
        else:
            return False

    def getTable(self):
        """
        Cette fonction renvoie la table de jeu
        :return: CardStack
        """
        return self.gameState.table

    ###################### HUD #################################

    def showDialogMessage(self, title, message, buttonText):
        self.gameState.dialog.popDialog(title, message, buttonText)

    def initDialog(self, title, msg, tbutton):
        self.initState.initDialog(title, msg, tbutton)

    ############################################################

    ########################## Fonctions de Jeu ###############################
    def playSelectedCard(self):
        action = self.getAction()
        self.playCard(action.originSprite)

    def getCurrentPlayerFirstCard(self):
        """ Retourne la première carte de la main du joueur courant si elle
        existe.

        :return (Card): Une Carte ou None
        """

        currentHand = self.getCurrentPlayerHand()

        if( len(currentHand) <= 0 ):
            raise PluginException("The number of players must be greater than 0.")

        return currentHand[0]

    def getCurrentPlayerPID(self):
        return self.currentTurn()

    ###########################################################################

    ######################### Table Functions ##################################

    def getLastCards(self, nb):
        """ Renvoie un tableu avec les nb dérnières cartes.

        :param nb (int):
        :return: CardStack
        """
        table = self.getTableCards()

        return table[len(table)-nb:len(table)]

    def getNbTableCards(self):
        """ Renvoie le nombre de cartes sur la table.

        :return (int):
        """

        return len(self.getTableDeck())

    ######################### /Table Functions #################################

    ######################### Deck Functions ##################################
    def isDeckEmpty(self):
        return not len(self.getTableDeck())

    ######################### /Deck Functions ##################################

    def getTableCards(self):
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
        if( hasattr(object,"getPid()") ):
            return object.getPid()

        else:
            print(object + " ne contient pas un pid.")

    def getTable(self):
        """
        Cette fonction renvoie la table de jeu
        :return: CardStack
        """
        return  self.gameState.table.table



    def getPlayerHand(self, pid):
        """
        Cette fonction renvoie ma main du joueur à partir d'un pid
        :param pid: int
        :return: CardStack
        """
        if (pid == -1 ): return  self.gameState.table.table
        return  self.gameState.table.getPlayerHand(pid)

    def getCurrentPlayerDeck(self):
        """ Renvoie le jeu de cartes du joueur
        :return (int):
        """

        return  self.gameState.table.players[self.currentTurn()].deck

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
        return  self.gameState.turn

    def getnbPlayers(self):
        return  self.gameState.table.nbPlayers


    def pickCardFrom(self, pid):
        """Déplace une carte du jeu de carte  pid à sa main

        :param pid (int): Le pid du joueur résponsable de l'action
        :return:
        """
        if(pid != -1):
            card =   self.gameState.getPlayer(pid).deck.pop()
        else:
            card =   self.gameState.table.deck.pop()

        self.gameState.getCurrentPlayerHand().append(card)

    def isPlayerTurn(self):
        return  self.gameState.turn == 0

    def flushTable(self):
        """ Efface le contenu de la table
        """

        self.gameState.table.flush()

    def playCard(self, card):
        oc = card
        od = self.currentTurn()
        dd = self.TABLE_PID

        self.gameState.moveCard(oc, od, dd)

    def isLost(self):
        return self.gameState.lose

    def isWin(self):
        return self.gameState.win

    def getCurrentPlayerHand(self):
        """ Retourne la main du joueur courant

        :return: un CardStack
        """
        return  self.gameState.getPlayerHand(self.currentTurn())

    def getPlayer(self, pid):
        """ Retourne un le PlayerState du joueur (pid)

        :param pid (int): Le pid du joueur que l'on veut obtenir
        :return: un PlayerState
        """
        return  self.gameState.table.players[pid]

    def getValeurCarte(self, carte):
        """ Renvoie la valeur de la carte selon les régles du jeu.

        :param carte (Card):
        :return: (int)
        """
        return self.gameState.cardValues[carte.value]

    def getAction(self):
        return self.agentAction

    def next_turn(self):
        """ Fonction qui passe le tourne
        """
        nb = self.gameState.getnbPlayers()
        tmp = (self.gameState.turn+1)
        resu = tmp % nb
        self.gameState.turn = resu

    def dealCards(self, nb_cards):
        """ Distribution de nb_cards en sens antihoraire
        :param nb_cards:
        :param deck_pid:
        """

        deck = self.gameState.table.deck

        for i in range(self.gameState.getnbPlayers()):
            carte = deck.pop()
            self.gameState.getPlayer(i).hand.append(carte)

###################### Score Functions #####################
    def getPlayerScore(self, pid):
        return self.getPlayer(pid).score

    def hasBestScore(self, pid):
        resu = True
        ps = self.getPlayerScore(pid)
        for i in range(self.getnbPlayers()):
            if(ps < self.getPlayerScore(i)):
                resu = False
        return resu

    def IHaveBestScore(self):
        return self.hasBestScore(self.getCurrentPlayerPID())

    def getCurrentPlayerScore(self):
        """ Renvoie le score du joueur
        :return (int):
        """

        return  self.gameState.getCurrentPlayer().score

    def getTableCardsPoints(self, inf=0, sup=None):
        """ Affecte au score du joueur courant la somme des valeurs des
        cartes d'index [inf, sup] ( toutes les cartes de la table si pas
        de paramètres.

        :param inf (int):
        :param sup (int):
        :return: None
        """
        if ( sup == None):
            sup=self.getNbTableCards()
        sum = self.getSumCardScore(inf, sup)
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
            sup=self.getNbTableCards()
        resu = 0



        for i in range( inf, sup):
            resu += self.getValeurCarte(self.getTableDeck()[i])

        return resu

    def addPlayerScore(self, pid, score):
         self.getPlayer(pid).score += score

######################      IA      ########################

    def defAgentAction(self, type,
                       originSprite=None, originDrawable=None):
        """ Cette fonction définit une action de l'opposant.

        :param type (String): Le type de l'action.
        :param originSprite (ClickableSprite): Un sprite d'origine.
        :param originDrawable (Drawable): Un drawable.
        :return: (Action): Une action.
        """

        action =  AgentAction( type)
        action.originSprite = originSprite
        action.originDrawable = originDrawable

        return action

######################      /IA      #######################



    def setCardValues(self, cardValues):
        """ Set the value of every card

        :param cardValues {card:value}
        :return: None
        """
        self.gameState.cardValues = cardValues


class IAPlugin(Player):
    def __init__(self, id):
        Player.__init__(self, id)

    def getAction(self, plugin):
        """ A implémenter dans le plugin.
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



    def initPlayers(self, nbPlayers):
        if( nbPlayers <= 0 ):
            raise PluginException("The number of players must be greater than 0.")
        for i in range(0,nbPlayers):
            self.addPlayerState(CardStack(), CardStack())

    def initDialog(self, title, msg, tbutton):
        self.dialog.popDialog(title, msg,tbutton)

    def addPlayerState(self, hand=CardStack(), deck=CardStack()):
        """ Ajoute un joueur au jeu
        :param hand: CardStack() la main initiale
        :param deck: CardStack() le jeu initial
        :return:
        """

        self.table.addPlayer( hand, deck)

    def generateShuffledDeck(self):
        """ Générer un jeu de cartes mélangé.

        :return: (CardStack)
        """

        deck = DeckGenerator.deckFactory()
        deck.shuffle()
        return deck

    def setCardValues(self, vals):
        self.cardValues = vals

    def setTableDeck(self, deck):
        """ Initialise le jeu de cartes de la table
        :param deck (CartStack):
        :return:
        """
        self.table.deck = deck
""" Autheur Giuseppe Federico 
"""
from basic_plugin.Plugin import Plugin
from environment.Card import Card
from environment.CardStack import CardStack
from environment.DeckGenerator import DeckGenerator
from game.InitState import InitState
from game.agents.Player import Player
from game.agents.AgentAction import AgentAction


class PluginBataille(Plugin):
    """ Cette classe représente un PluginBataille 
    """

    def __init__(self):
        Plugin.__init__(self)


    def initGameState(self):
        """
        Cette fonction initialise l'état intitial du jeu
        La table et les joueurs.
        :return:
        """
        # Initialisation du jeu
        init_state = InitState()

        # Initialisation du joueur1

        # On initialise la main initiale

        ##### INIT PLAYER 1 ######
        deck_player1 = DeckGenerator.deckFactory()
        deck_player1.shuffle()

        hand_player1 = CardStack()
        for i in range(4):
            hand_player1.append(deck_player1.pop())


        init_state.addPlayerState(hand_player1, deck_player1)
        ###########################

        ##### INIT PLAYER 2 ######
        carte1 = Card(1, "red", "c")
        carte2 = Card(4, "red", "c")


        deck_player2 = DeckGenerator.deckFactory()
        deck_player2.shuffle()
        hand_player2 = CardStack()
        for i in range(4):
            hand_player2.append(deck_player2.pop())

        init_state.addPlayerState(hand_player2, deck_player2)
        ###########################

        ######## INIT TABLE ########
        init_state.table.table.append(carte1)
        ############################

        ######## INIT OPPONENT ##########
        self.opponents.append( IABataille() )
        #################################


        return init_state

    def nextState(self, gameState, agent_action):
        """ This is a function
        """
          #TODO: à implémenter
        """  Renvoie le prochain etat du jeu etant donnée une action
        """

        new_state = gameState.copy()

        # Boujer une carte
        if(agent_action.type == "move"):
            oc = agent_action.originSprite
            od = agent_action.originDrawable
            dd = agent_action.dest_deck

            new_state.moveCard(oc, od, dd)

        new_state.next_turn()


        return new_state


    def isLegalMove(self, gameState, agent_action):
        #TODO: à implémenter
        """
        Renvoie True si l'action est legale dans l'état courant
        :param agent_action:
        :param plugin:
        :return:
        """


        #TODO: vérifier que ce soit une carte qu'on clicque
        # Cas d'un move
        if( agent_action.type == "move"):
            #if( agent_action.dest_deck != self.TABLE_PID ):
            #    print("Mauvaise destination")
            #    return False
            if( agent_action.originDrawable != gameState.currentTurn() ):
                print("C'est pas le tourn de " + str(agent_action.origin_deck))
                return False

        return True

class IABataille(Player):
    def __init__(self):
        Player.__init__(self, 1)

    def getAction(self, agent_state, game_state, event=None):
        hand = game_state.table.getPlayerHand(self.id)

        #TODO: à terminer
        card = hand[0]


        action = AgentAction(0, "move")
        action.originSprite = card
        action.origin_deck = game_state.turn
        action.dest_deck = -1

        return action


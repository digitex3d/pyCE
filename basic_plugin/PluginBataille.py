""" Autheur Giuseppe Federico 
"""
from basic_plugin.Plugin import Plugin
from environment.Card import Card
from environment.CardStack import CardStack
from game.InitState import InitState


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
        carte1 = Card(1, "red", "c")
        carte2 = Card(2, "red", "c")

        hand_player1 = CardStack()
        hand_player1.append(carte1)
        hand_player1.append(carte2)

        init_state.addPlayerState(hand_player1)
        ###########################

        ##### INIT PLAYER 2 ######
        carte1 = Card(1, "red", "c")
        carte2 = Card(4, "red", "c")

        hand_player2 = CardStack()
        hand_player2.append(carte1)
        hand_player2.append(carte2)

        init_state.addPlayerState(hand_player2)
        ###########################

        ######## INIT TABLE ########
        init_state.table.table.append(carte1)
        ############################

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
            oc = agent_action.origin_card
            od = agent_action.origin_deck
            dd = agent_action.dest_deck

            gameState.moveCard(oc, od, dd)


    def isLegalMove(self,gameState, agent_action):
         return True
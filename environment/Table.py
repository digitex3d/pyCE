""" Cette classe représente une Table """

from environment.CardStack import CardStack


class Table():

    def __init__(self):
        """
        Cette classe représente l'état d'une table, les joueurs et les cartes sur
        la table.
        :return:
        """
        self.players = []
        self.table = CardStack()
        self.nbPlayers = 0

    def addPlayer(self, playerState):
        """
        Fonction qui ajoute un joueur à la table
        :param playerState: PlayerState
        :return:
        """
        self.nbPlayers += 1
        self.players.append(playerState)

    def getPlayerHand(self, pid):
        """
        Cette fonction renvoie ma main du joueur CardStack à partir d'un pid
        :param pid: int
        :return: CardStack
        """
        return self.players[pid].hand



    def __str__(self):
        string = "["
        for index, item in enumerate(self):
            string += str(item)
            if index != len(self)-1:
                string += ", "
        return string + "]"


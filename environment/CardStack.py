""" Cette classe représente un jeu de cartes """

from random import shuffle

class CardStack(list):
    """ On melange le jeu de cartes """
    def shuffle(self):
        shuffle(self)

    """ Renvoie la dernière carte du jeu de carte """
    def getLast(self):
        return self[self.size()-1]

    """ La taille du jeu de carte """
    def size(self):
        return len(self)


    def isEmpty(self):
        """ Renvoie True si le CardStack est vide, false sinon.

        :return (boolean):
        """
        if not self.table:
            return True
        else:
            return False
        
    def __str__(self):
        string = "["
        for index, item in enumerate(self):
            string += str(item)
            if index != len(self)-1:
                string += ", "
        return string + "]"

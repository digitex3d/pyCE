""" Autheur Giuseppe Federico 
"""


class Utils:
    """ Classe utilitaire pour la GUI
    """

    #TODO: terminer
    def alignCenterBy(self, conteneur, contenu):
        """
        Cette fonction déplace le contenu au centre du conteneur
        :param conteneur: Un objet qui à des coordonnes et une dimension
        :param contenu: Un objet qui à des coordonnes et une dimension
        :return:
        """

        contenu.x = conteneur.x+conteneur.width/2
        contenu.y = conteneur.y+conteneur.height/2


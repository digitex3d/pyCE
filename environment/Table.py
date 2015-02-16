""" Cette classe représente une Table """


class Table(list):
    """ Nombre de joue de cartes dans une table"""
    def size(self):
        return len(self)

    def __str__(self):
        string = "["
        for index, item in enumerate(self):
            string += str(item)
            if index != len(self)-1:
                string += ", "
        return string + "]"


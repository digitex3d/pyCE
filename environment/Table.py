""" Cette classe représente une Table """


class Table():
    """ Cette classe représésente une table"""
    def size(self):
        return len(self)

    def __str__(self):
        string = "["
        for index, item in enumerate(self):
            string += str(item)
            if index != len(self)-1:
                string += ", "
        return string + "]"


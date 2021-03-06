class Card:
    """ Une carte
     """

    def __init__(self, value="None", color="None", kind="None"):
        self.value = value
        self.color = color
        self.kind = kind
        self.hidden = False
        self.owner = -1

    def flipCard(self):
        """ Cacher/Monter la carte.
        """
        self.hidden = not self.hidden

    def __str__(self):
        return "[ value =" + str(self.value) +\
                " color =" + str(self.color) +\
                " kind = " + str(self.kind) +"]"


class Card:
    KINDS = []

    def __init__(self, value="None", color="None", kind="None"):
        self.value = value
        self.color = color
        self.kind = kind

    def __str__(self):
        return "[ value =" + str(self.value) +\
                " color =" + str(self.color) +\
                " kind = " + str(self.kind) +"]"
class Dialog:
    """ Une section pour les messages
     """

    def __init__(self):
        self.textButton = ""
        self.message = ""
        self.title = ""
        self.visible = False

    def popDialog(self, title, message, tbutton):
        self.textButton = tbutton
        self.message = message
        self.title = title
        self.visible = True

    def hideDialog(self):
        self.visible = False

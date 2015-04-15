class Dialog:
    """ Une section pour les messages
     """

    def __init__(self):
        self.textButton = ""
        self.message = ""
        self.title = ""
        self.action = ""
        self.visible = False

    def popDialog(self, title, message, tbutton, action):
        self.textButton = tbutton
        self.message = message
        self.title = title
        self.visible = True
        self.action = action

    def hideDialog(self):
        self.visible = False

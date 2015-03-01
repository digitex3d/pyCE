


class AgentAction:
    """ Cette classe représente une action """

    def __init__(self, id, type):
        self.player_id = id
        self.type = None
        self.origin= None
        self.dest = None
        self.deck = None



class AgentAction:
    """ Cette classe représente une action """

    def __init__(self, id, type):
        self.player_id = id
        self.type = type
        self.originDrawable= None
        self.dest_deck = None
        self.originSprite = None

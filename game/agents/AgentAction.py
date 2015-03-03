


class AgentAction:
    """ Cette classe représente une action """

    def __init__(self, id, type):
        self.player_id = id
        self.type = type
        self.origin_deck= None
        self.dest_deck = None
        self.origin_card = None
        self.dest_card = None
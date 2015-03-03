from game.agents.AgentAction import AgentAction

class Agent:
    """ Cette classe représente un Agent """

    def __init__(self, id=0):
        self.id = id

    def getAction(self, agent_state, game_state, event=None):
        """ Renvoie une action de l'agent
        """



        #TODO: modifier l'id
        if( not event.isFull() ):
            action = AgentAction(0, "none")
            return action

        action = AgentAction(0, "move")
        action.origin_card = event.card_clicked.card
        action.origin_deck = event.cardStack_clicked.cardStack
        action.dest_deck = event.cardStack_released.cardStack

        return action




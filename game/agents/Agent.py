from game.agents.AgentAction import AgentAction

class Agent:
    """ Cette classe représente un Agent """

    def __init__(self, id=0):
        self.id = id

    def getAction(self, agent_state, game_state, event=None):
        """ Renvoie une action de l'agent
        """
        action = AgentAction(0, "move")
        action.origin = event.card_clicked
        action.dest = event.cardStack_released
        return action;

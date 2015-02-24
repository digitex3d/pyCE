from game.agents.AgentAction import AgentAction

class Agent:
    """ Cette classe représente un Agent """

    def __init__(self, id=0):
        self.id = id

    def getAction(self, agent_state, game_state):
        return AgentAction()

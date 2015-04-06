from game.agents.AgentAction import AgentAction
from gui.Drawables.CardStackDrawable import CardStackDrawable
from gui.Drawables.DeckDrawable import DeckDrawable


class Player:
    """ Cette classe représente un Agent """

    def __init__(self, id=0):
        self.id = id

    def getAction(self, agent_state, game_state, event=None):
        """ Renvoie une action de l'agent
        """

        actions = []

        if( not event.isFull() ):
            action = AgentAction(0, "none")
            return []

        if hasattr(event.spriteClicked, 'card'):
            move = AgentAction(0, "move")
            move.originSprite = event.spriteClicked.card
            move.originDrawable = event.drawableClicked.pid
            move.dest_deck = event.drawableReleased.pid
            actions.append(move)

        if( event.drawableClicked.name == "Deck" ):
            actions.append(AgentAction(0, "pick"))

        return actions




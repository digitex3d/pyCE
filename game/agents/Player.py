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

        #TODO: modifier l'id
        if( not event.isFull() ):
            action = AgentAction(0, "none")
            return []

        if( event.drawableClicked.name == "Deck" ):
            actions.append(AgentAction(0, "pick"))

        elif ( event.drawableClicked.name == "CardStack" ):
            move = AgentAction(0, "move")
            move.originSprite = event.spriteClicked.card
            move.originDrawable = event.drawableClicked.pid
            move.dest_deck = event.drawableReleased.pid
            actions.append(move)
        return actions




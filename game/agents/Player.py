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

        if hasattr(event.spriteClicked, 'card'):
            move = AgentAction("move")
            move.originSprite = event.spriteClicked.card
            move.originDrawable = event.drawableClicked.pid
            move.dest_deck = event.drawableReleased.pid
            return move
        elif (hasattr(event.drawableClicked, 'name')):
            if ( event.drawableClicked.name == "Dialog" ):
                dialog = AgentAction("dialog")
                return dialog
        else:
            return AgentAction("None")




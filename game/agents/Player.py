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



        #TODO: modifier l'id
        if( not event.isFull() ):
            action = AgentAction(0, "none")
            return action

        if( type(event.drawableClicked) is DeckDrawable ):
            action = AgentAction(0, "pick")
        elif ( type(event.drawableClicked) is CardStackDrawable ):
            action = AgentAction(0, "move")
            action.originSprite = event.spriteClicked.card
            action.originDrawable = event.drawableClicked.pid
            action.dest_deck = event.drawableReleased.pid

        return action




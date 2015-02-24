""" Autheur Giuseppe Federico 
"""
from basic_plugin.SpriteFactory import SpriteFactory
from gui.CardStackDrawable import CardStackDrawable
class TableDrawable:
    """ Cette classe représente un TableDrawable 
    """

    def __init__(self, game_state):
        # La liste des Sprites qui composent la table
        self.game_state = game_state
        self.drawableHands = []
        self.setUp()


    def setUp(self):
         for agent in self.game_state.agentsStates:
             self.addHand( agent.hand, agent.id )


    def addHand(self, cardStack, proprietary):
        """ This is a function
        """

        drawableHand =  CardStackDrawable(SpriteFactory.deck_factory(cardStack),
                                          proprietary,
                                          500 ,
                                          500)

        self.drawableHands.append(drawableHand)

    def getSprites(self):
        sprites = []
        for drawableHand in self.drawableHands:
            sprites.extend(drawableHand.cardSprites)

        return sprites



    def update(self, game_state):
        """ Fonction qui va mettre à jour les sprites de la table
        """

        # On met à jour les mains des joueurs
        for cardStack in self.drawableHands:
            cardStack.update(game_state.agentsStates[cardStack.proprietary].hand)


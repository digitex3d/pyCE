""" Autheur Giuseppe Federico 
"""
from gui.SpriteFactory import SpriteFactory
from gui.CardStackDrawable import CardStackDrawable
from environment.CardStack import CardStack
class TableDrawable:
    """ Cette classe représente un TableDrawable 
    """

    def __init__(self, game_state):
        # La liste des Sprites qui composent la table
        self.game_state = game_state
        self.drawableHands = []
        self.nb_hands = 0
        self.tableStack = CardStackDrawable()
        self.setUp()



    def setUp(self):
         for agent in self.game_state.agentsStates:
             self.addHand( agent.hand, agent.id )


    def addHand(self, cardStack, proprietary):
        """ This is a function
        """
        if( self.nb_hands == 0):
            drawableHand =  CardStackDrawable(cardStack,
                                              proprietary,
                                              500 ,
                                              500)
        if( self.nb_hands == 1):
            drawableHand =  CardStackDrawable(cardStack,
                                              proprietary,
                                              100 ,
                                              100)

        self.drawableHands.append(drawableHand)
        self.nb_hands += 1;

    def getSprites(self):
        sprites = []
        for drawableHand in self.drawableHands:
            sprites.extend(drawableHand.cardSprites)
        sprites.append( self.tableStack.cardSprites)
        return sprites

    def get_hands(self):
        return self.drawableHands


    def update(self, game_state):
        """ Fonction qui va mettre à jour les sprites de la table
        """

        # On met à jour les mains des joueurs
        for cardStack in self.drawableHands:
            cardStack.update(game_state.agentsStates[cardStack.proprietary].hand)


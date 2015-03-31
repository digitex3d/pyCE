from gui.Sprites.CardSprite import CardSprite

IMG_FORMAT="gif"
DATA_PATH="data"

class SpriteFactory():
    def card_factory(card, x=0, y=0, blend_src=770, blend_dest=771, batch=None, group=None, usage='dynamic'):
        file_name = str(card.value) + str(card.kind) + "." + IMG_FORMAT
        img = DATA_PATH+"/cards/"+file_name

        return CardSprite(card,img, x, y, blend_src, blend_dest, batch, group, usage)

    card_factory = staticmethod(card_factory)

    def deck_factory(cards):
        """ Renvoie une liste de CardSprite
        """
        cardSprites = []
        for card in cards:
            cardSprites.append(SpriteFactory.card_factory(card))
        return cardSprites

        """ Fonction accessoire qui génere une main aléatoire

        #TODO: Terminer d'implementer et déplacer
        randDeck = CardStack()

        for i in range(nb_cards):
            randDeck.append( Card())
            """
    deck_factory = staticmethod(deck_factory)





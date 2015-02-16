""" Cette classe représente une CardSpriteFactory pour génerer des sprites"""

from gui.CardSprite import CardSprite
from gui.CardStackDrawable import CardStackDrawable
import pyglet
IMG_FORMAT="gif"
DATA_PATH="data"

class SpriteFactory():
    def card_factory(card, x=0, y=0, blend_src=770, blend_dest=771, batch=None, group=None, usage='dynamic'):
        file_name = str(card.value) + str(card.kind) + "." + IMG_FORMAT
        img = DATA_PATH+"/cards/"+file_name

        return CardSprite(card,img, x, y, blend_src, blend_dest, batch, group, usage)

    card_factory = staticmethod(card_factory)

    def deck_factory(cards,x=0,y=0):
        dcards_list = []
        batch = pyglet.graphics.Batch()

        for card in cards:
            dcards_list.append(SpriteFactory.card_factory(card,batch=batch))
        return CardStackDrawable(dcards_list,batch,x,y)





import pyglet
import basic_plugin
from environment.Card import Card
from basic_plugin.SpriteFactory import SpriteFactory
from gui.CardStackDrawable import CardStackDrawable

window = pyglet.window.Window(800, 600)

pos = 50
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

cards = []



cards.append(Card(7,"red","h"))
cards.append(Card("k","red","s"))
cards.append(Card("j","red","c"))
cards.append(Card(3,"red","h"))
cards.append(Card(9,"red","h"))
cards.append(Card(10,"red","h"))



deck = SpriteFactory.deck_factory(cards,50,50)
deck.set_up()

def update(dt):
    deck.drawableCards[0].switch_side()
pyglet.clock.schedule_interval(update, 1)

@window.event
def on_key_press(symbol, modifiers):
    print("A key was pressed")

@window.event
def on_draw():
    print("Drawing screen")
    window.clear()
    label.draw()
    deck.batch.draw()


if __name__ == '__main__':
    pyglet.app.run()

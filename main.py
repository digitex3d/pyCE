import pyglet
import basic_plugin
from environment.Card import Card
from basic_plugin.SpriteFactory import SpriteFactory
from gui.CardStackDrawable import CardStackDrawable
from game.InitState import InitState
from game.agents.AgentState import AgentState
from game.GameState import GameState
from game.Game import Game
from basic_plugin.ScoreAddAgent import ScoreAddAgent
from gui.HUD import HUD
window = pyglet.window.Window(800, 600)




cards = []

cards.append(Card(7,"red","h"))
cards.append(Card("k","red","s"))
cards.append(Card("j","red","c"))
cards.append(Card(3,"red","h"))
cards.append(Card(9,"red","h"))
cards.append(Card(10,"red","h"))

deck = SpriteFactory.deck_factory(cards,0,0,"v")
deck.set_up()

hud = HUD(window)

init_state = InitState()
player_state = AgentState(0,1)
init_state.addAgentState(player_state)
game_state = GameState(init_state)
game = Game(game_state)
agent = ScoreAddAgent()
game.addAgent(agent)
game.addObserver(hud)
game.run()



def update(dt):
    deck[3].switch_side()
pyglet.clock.schedule_interval(update, 1)

@window.event
def on_key_press(symbol, modifiers):
    print("A key was pressed")

@window.event
def on_draw():
    print("Drawing screen")
    window.clear()
    # Afficher une main
    for card in deck:
        card.draw()
    for component in hud.hud_components:
        component.draw()


if __name__ == '__main__':
    pyglet.app.run()

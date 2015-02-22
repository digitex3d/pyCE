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
from gui.MainGameWindow import MainGameWindow

window = MainGameWindow()
hud = HUD(window)

window.add_component(hud)

init_state = InitState()
player_state = AgentState(0,1)
init_state.addAgentState(player_state)
game_state = GameState(init_state)
game = Game(game_state)
agent = ScoreAddAgent()
game.addAgent(agent)
game.addObserver(window)
game.run()


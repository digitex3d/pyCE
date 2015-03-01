from environment.Card import Card
from game.InitState import InitState
from game.agents.AgentState import AgentState
from game.GameState import GameState
from game.Game import Game

from game.agents.Agent import  Agent
from gui.HUD import HUD
from gui.MainGameWindow import MainGameWindow
from environment.CardStack import *
from gui.TableDrawable import TableDrawable

# Initialisation du jeu
init_state = InitState()

# Initialisation du joueur1

# On initialise la main initiale

carte1 = Card(1, "red", "c")
carte2 = Card(2, "red", "c")

hand_player1 = CardStack()
hand_player1.append(carte1)
hand_player1.append(carte2)

player1_state = AgentState(0,hand_player1)
init_state.addAgentState(player1_state)

# On initialise le jeu
game_state = GameState(init_state)
game = Game(game_state)

agent = Agent(0)
game.addAgent(agent)

# On initialise la fenetre principale
window = MainGameWindow(game)
hud = HUD(window)
table = TableDrawable(game.game_state)

window.add_component(hud)
window.add_component(table)
game.addObserver(window)

window.main_loop()


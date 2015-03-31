from environment.Card import Card
from game.InitState import InitState
from game.agents.PlayerState import PlayerState
from game.GameState import GameState
from game.Game import Game
from gui.Components.HUDComponent import HUDComponent
from gui.Components.TableComponent import TableComponent
from game.agents.Agent import  Agent
from gui.MainGameWindow import MainGameWindow
from environment.CardStack import *
from gui.Drawables import TableDrawable



# Initialisation du jeu
init_state = InitState()

# Initialisation du joueur1

# On initialise la main initiale

##### INIT PLAYER 1 ######
carte1 = Card(1, "red", "c")
carte2 = Card(2, "red", "c")

hand_player1 = CardStack()
hand_player1.append(carte1)
hand_player1.append(carte2)

player1_state = PlayerState(1,hand_player1)
init_state.addPlayerState(player1_state)
###########################

##### INIT PLAYER 2 ######
carte1 = Card(1, "red", "c")
carte2 = Card(4, "red", "c")

hand_player2 = CardStack()
hand_player2.append(carte1)
hand_player2.append(carte2)

player2_state = PlayerState(2,hand_player2)
init_state.addPlayerState(player2_state)
###########################

######## INIT TABLE ########
init_state.table.table.append(carte1)
############################

# On initialise le jeu
game_state = GameState(init_state)
game = Game(game_state)

agent = Agent(0)
game.addAgent(agent)

# On initialise la fenetre principale
window = MainGameWindow(game, 1024, 768)
hud = HUDComponent(window)
table = TableComponent(window)

window.add_component(hud)
window.add_component(table)
table.setUp(game_state)
game.addObserver(window)
table.update(game_state)

window.main_loop()


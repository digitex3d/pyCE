
from environment.Card import Card
from game.InitState import InitState
from game.agents.PlayerState import PlayerState
from game.GameState import GameState
from game.Game import Game
from gui.Components.HUDComponent import HUDComponent
from gui.Components.TableComponent import TableComponent
from game.agents.Player import  Player
from gui.MainGameWindow import MainGameWindow
from environment.CardStack import *
from gui.Drawables import TableDrawable
import sys
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)







if len(sys.argv) > 1:
    plugin_name = str(sys.argv[1])
else:
    print("Usage: pyCE plugin_name")
    exit(0)

# On importe le plugin passé en argument, de cette façon
# on pourra importer le plugin à tout moment au runtime
# avec la fonction __import__
def my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

mod = my_import("plugins.%s" % plugin_name +".PluginInit")
plugin = mod.PluginInit()






# On initialise le jeu
game_state = GameState(plugin.initGameState(), plugin)
game = Game(game_state)

player = Player(0)
game.addAgent(player)
ia = plugin.opponents[0]
game.addAgent(ia)

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


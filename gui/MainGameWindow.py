""" Autheur Giuseppe Federico 
"""

from pyglet import window
from pyglet import clock
from pyglet import font
from game.Event import Event

class MainGameWindow(window.Window):
    def __init__(self,  game, *args, **kwargs):
        #Let all of the standard stuff pass through
        window.Window.__init__(self, *args, **kwargs)
        self.components = []
        self.game = game

    def add_component(self, component):
        self.components.append(component)

    def main_loop(self):
        """ La boucle principale du jeu
        """

        # FPS
        ft = font.load('Arial', 28)
        fps_text = font.Text(ft, y=10)

        while not self.has_exit:
            self.dispatch_events()
            self.clear()

            self.draw()

            #Tick the clock
            clock.tick()
            #Gets fps and draw it
            fps_text.text = ("fps: %d") % (clock.get_fps())
            fps_text.draw()
            self.flip()

    def update(self, game_state=None):
        print("Drawing screen")
        self.dispatch_events()
        self.clear()

        for component in self.components:
            component.update(game_state)

        self.draw()
        #Tick the clock
        clock.tick()
        self.flip()

    """ ############	Event Handlers      ############
    """
    def on_mouse_press(self, x, y, dx, dy):
        event = Event("mouse_click")
        event.add_mouse_coords(x,y)
        self.game.eventHandler(event)

    def draw(self):
        for component in self.components:
            for sprite in component.sprites:
                sprite.draw()
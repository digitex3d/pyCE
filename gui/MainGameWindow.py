""" Autheur Giuseppe Federico 
"""

from pyglet import window
from pyglet import clock
from pyglet import font

class MainGameWindow(window.Window):
    def __init__(self, *args, **kwargs):
        #Let all of the standard stuff pass through
        window.Window.__init__(self, *args, **kwargs)
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def update(self, game_state):
        print("Drawing screen")
        self.dispatch_events()
        self.clear()

        ft = font.load('Arial', 28)
        fps_text = font.Text(ft, y=10)
        for component in self.components:
            component.update(game_state)

        self.draw()

        #Tick the clock
        clock.tick()
        #Gets fps and draw it
        fps_text.text = ("fps: %d") % (clock.get_fps())
        fps_text.draw()
        self.flip()

    def draw(self):
        for component in self.components:
            for sprite in component.sprites:
                sprite.draw()
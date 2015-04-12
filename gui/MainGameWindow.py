""" Autheur Giuseppe Federico 
"""

#TODO: TERMINER

from pyglet import window
from pyglet import clock
from pyglet import font
import pyglet
from pyglet.sprite import Sprite
from game.Event import Event
import logging
from gui.Default import DATA_PATH


class MainGameWindow(window.Window):
    def __init__(self, game, *args, **kwargs):
        #Let all of the standard stuff pass through
        window.Window.__init__(self, *args, **kwargs)
        self.components = []
        self.game = game
        self.last_event = None

    def add_component(self, component):
        self.components.append(component)

    def main_loop(self):
        """ La boucle principale du jeu
        """

        # FPS
        ft = font.load('Arial', 28)
        fps_text = font.Text(ft, y=10)

        while not (self.has_exit):
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
        self.last_event = Event("mouse_click")
        self.last_event.add_mouse_coords(x,y)

        for component in self.components:
            if component.isClicked(x,y):
                self.last_event.componentClicked = component
            for drawable in component.getDrawables():
                if drawable.isClicked(x,y):
                    self.last_event.drawableClicked = drawable
                for sprite in drawable.getSprites():
                    if("isClicked" in dir(sprite) and
                           sprite.isClicked(x,y)):
                        self.last_event.spriteClicked = sprite

        logging.info('Mouse press: X:%s Y:%s',x ,y )
        logging.debug(self.last_event)

    def on_mouse_release(self, x, y, button, modifiers):
        for component in self.components:
            if component.isClicked(x,y):
                self.last_event.componentReleased = component
            for drawable in component.getDrawables():
                if drawable.isClicked(x,y):
                    self.last_event.drawableReleased = drawable
                for sprite in drawable.getSprites():
                    if("isClicked" in dir(sprite) and
                           sprite.isClicked(x,y)):
                        self.last_event.spriteReleased = sprite

        logging.debug(self.last_event)
        logging.info('Mouse release: X:%s Y:%s',x ,y )
        self.game.eventHandler(self.last_event)
        self.last_event = None

    def draw(self):
        # Background
        background = pyglet.image.load(DATA_PATH + "table/table.jpg")
        Sprite(background,0,0).draw()

        for component in self.components:
            for drawable in component.getDrawables():
                for sprite in drawable.getSprites():
                    sprite.draw()








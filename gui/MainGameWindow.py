""" Autheur Giuseppe Federico 
"""

from pyglet import window
from pyglet import clock
from pyglet import font
from game.Event import Event


class MainGameWindow(window.Window):
    def __init__(self, game, height=768, width=1024, *args, **kwargs):
        #Let all of the standard stuff pass through
        window.Window.__init__(self, height=768, width=1024, *args, **kwargs)
        self.components = []
        self.game = game
        self.height = height
        self.width = width
        self.last_event = None

    def add_component(self, component):
        self.components.append(component)

    def main_loop(self):
        """ La boucle principale du jeu
        """

        # FPS
        ft = font.load('Arial', 28)
        fps_text = font.Text(ft, y=10)

        while not (self.has_exit or self.game.game_state.win):
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
            if("get_hands" in dir(component)):
                for hand in component.get_hands():
                    if(hand.isClicked(x,y)):
                        self.last_event.cardStack_clicked = hand

            for sprite in component.getSprites():
                if("isClicked" in dir(sprite) ):
                    if(sprite.isClicked(x,y)):
                        self.last_event.card_clicked = sprite

    def on_mouse_release(self, x, y, button, modifiers):
        self.last_event.add_mouse_coords(x,y)
        for component in self.components:
            if("get_hands" in dir(component)):
                for hand in component.get_hands():
                    if(hand.isClicked(x,y)):
                        self.last_event.cardStack_released = hand

            for sprite in component.getSprites():
                if("isClicked" in dir(sprite) ):
                    if(sprite.isClicked(x,y)):
                        self.last_event.card_released = sprite


        self.game.eventHandler(self.last_event)
        self.last_event = None

    def draw(self):
        for component in self.components:
            for sprite in component.getSprites():
                if("draw" in dir(sprite) ):
                    sprite.draw()

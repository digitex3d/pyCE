""" Autheur Giuseppe Federico 
"""
from xxsubtype import spamdict


class Event:
    """ Cette classe représente un Event 
    """

    def __init__(self, type):
        self.type = type
        self.mouse_coords = []
        self.spriteClicked = None
        self.drawableClicked = None
        self.componentClicked = None
        self.spriteReleased = None
        self.drawableReleased = None
        self.componentReleased = None

    def add_mouse_coords(self, x , y):
        self.mouse_coords.append((x,y))

    def isFull(self):
        return  self.spriteClicked != None and \
        self.drawableClicked != None and \
        self.spriteReleased != None and \
        self.drawableReleased != None

    def __str__(self):
        return "[type=" + self.type + "\n" + \
               "coords=" + str(self.mouse_coords) + "\n" + \
               "card_clicked=" + str(self.spriteClicked) + "\n" + \
               "cardStack_clicked=" + str(self.drawableClicked) + "\n" + \
               "card_released=" + str(self.spriteReleased) + "\n" + \
               "cardStack_released=" + str(self.drawableReleased) + "]\n"

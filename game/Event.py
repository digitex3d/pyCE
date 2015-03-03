""" Autheur Giuseppe Federico 
"""
from xxsubtype import spamdict


class Event:
    """ Cette classe représente un Event 
    """

    def __init__(self, type):
        self.type = type
        self.mouse_coords = []
        self.card_clicked = None
        self.cardStack_clicked = None
        self.card_released = None
        self.cardStack_released = None

    def add_mouse_coords(self, x , y):
        self.mouse_coords.append((x,y))

    def isFull(self):
        return  self.card_clicked != None and \
        self.cardStack_clicked != None and \
        self.card_released != None and \
        self.cardStack_released != None

    def __str__(self):
        return "[type=" + self.type + "\n" + \
               "coords=" + str(self.mouse_coords) + "\n" + \
               "card_clicked=" + str(self.card_clicked) + "\n" + \
               "cardStack_clicked=" + str(self.cardStack_clicked) + "\n" + \
               "card_released=" + str(self.card_released) + "\n" + \
               "cardStack_released=" + str(self.cardStack_released) + "]\n"

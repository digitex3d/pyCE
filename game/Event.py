""" Autheur Giuseppe Federico 
"""


class Event:
    """ Cette classe représente un Event 
    """

    def __init__(self, type):
        self.type = type
        self.mouse_coords = []

    def add_mouse_coords(self, x , y):
        self.mouse_coords.append((x,y))
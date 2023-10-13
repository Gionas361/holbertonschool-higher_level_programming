#!/usr/bin/python3
"""Not Empty rectangle class"""


class Rectangle:
    """Makes a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize this b*tch"""
        pass

    @property
    def width(self):
        """Setting width"""
        self.width = self

    @width.setter
    def width(self, value):
        """Checking width is valid"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")

    @property
    def height(self):
        """Setting height"""
        self.height = self

    @height.setter
    def height(self, value):
        """Checking height is valid"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")

#!/usr/bin/python3
"""Not Empty rectangle class"""


class Rectangle:
    """Makes a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize this b*tch"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Setting width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Checking width is valid"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = self

    @property
    def height(self):
        """Setting height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Checking height is valid"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = self

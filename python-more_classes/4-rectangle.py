#!/usr/bin/python3
"""Not Empty rectangle class"""


class Rectangle:
    """Makes a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize this b*tch"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Setting width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if not value >= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Setting height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not value >= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Gets the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Gets the perimiter"""
        if self.__width <= 0 or self.__height <= 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """Prints the rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Print rectangle with the size"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

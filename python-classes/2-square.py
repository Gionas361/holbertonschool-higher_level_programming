#!/usr/bin/python3
"""Define a class named SQUARE"""


class Square:
    """S Q U A R E."""

    def __init__(self, size=0):
        """Start new square"""
        if not isinstance(size, int):
            TypeError("size must be an integer")
        elif size < 0:
            ValueError("size must be >= 0")
        else:
            self.__size = size


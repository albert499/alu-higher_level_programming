#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a class Rectangle that inherits from BaseGeometry."""
=======
"""9-rectangle.py
"""


>>>>>>> d1be129831ed9fae942d0d3643bb1870619788bf
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
<<<<<<< HEAD
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
=======
    """ Rectangle inherits from BaseGeomtry """

    def __init__(self, width, height):
        """ Constructor """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns area of Rectangle object"""
        return self.__width * self.__height

    def __str__(self):
        """ string represention of Rectangle object """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
>>>>>>> d1be129831ed9fae942d0d3643bb1870619788bf

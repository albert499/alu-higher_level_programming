#!/usr/bin/python3
<<<<<<< HEAD
"""inherits from BaseGeometry"""


class BaseGeometry:
    """public instance method"""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialization of privates"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
=======
"""8-rectangle.py
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inherits from BaseGeomtry """

    def __init__(self, width, height):
        """ Constructor"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
>>>>>>> d1be129831ed9fae942d0d3643bb1870619788bf
        self.__height = height

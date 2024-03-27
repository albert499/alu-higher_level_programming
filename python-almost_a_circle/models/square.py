#!/usr/bin/python3
"""Defines Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines square class and the methods"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization on the sqaure method

        Args:
            size (int): width and height
            x (int): the x
            y (int): the y
            id (int) = the id
            """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Print using __str__ function"""
        my_str = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return (my_str)

    def update(self, *args, **kwargs):
        """update the class Rectangle def update(self, *args)
        Args:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        Raises: No error
        Retuirns: the newe values"""

        if args != 0 and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        else:
            for k, v in kwargs.items():
                if k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
                elif k == "id":
                    self.id = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

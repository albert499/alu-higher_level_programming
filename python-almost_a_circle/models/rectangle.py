#!/usr/bin/python3
"""Base class"""
from models.base import Base


class Rectangle(Base):
    """Implimenting Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisation

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Compute area"""
        return (self.width * self.height)

    def display(self):
        """Displays the Rectangle using the `#` character."""
        for y in range(self.__y):
            print()
        for h in range(self.height):
            for x in range(self.__x):
                print(" ", end="")
            print("#" * self.width)

    def __str__(self):
        """Print using __str__ function"""
        my_str = f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
        my_str = my_str + f"{self.width}/{self.height}"
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
                    super().__init__(args[0])
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        else:
            for k, v in kwargs.items():
                if k == "id":
                    super().__init__(v)
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

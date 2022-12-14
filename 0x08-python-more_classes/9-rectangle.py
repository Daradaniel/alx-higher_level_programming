#!/usr/bin/python3
"""This module  has a class for rectangule instances.
The module has the class Rectangle.
"""


class Rectangle:
    """class rectangle.
    the class defines the height and width prived
    instance attributes, getter and setter method for each.
    __repr__ to be print with print() and str()
    __del__ method implementation, public class attribute
    number_of_instances, public class attribute print_symbol
    static method bigger_or_equal.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = Rectangle.print_symbol
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    def area(self):
        return (self.width * self.height)
        
    def perimeter(self):
        if (self.height == 0 or self.width == 0):
            return 0
        else:
            return 2 * self.height + 2 * self.width
        
    def __str__(self):
        if (self.height != 0 and self.width != 0):
            a = self.width * "#" + "\n"
            b = self.width * "#"
            return ((self.height - 1) * a + b)
        else:
            return ("")

    def __repr__(self):
        Rectangle.number_of_instances -= 1
        return "Rectangle({}, {})".format(self.width, self.height)
    
    def __del__(self):
        print("Bye Rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (isinstance(rect_1, Rectangle) is False):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (isinstance(rect_2, Rectangle) is False):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif (rect_1.area() >= rect_2.area()):
            return(rect_1)
        else:
            return(rect_2)

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

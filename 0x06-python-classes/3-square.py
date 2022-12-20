#!/usr/bin/python3

"""
class: Square

python3 -c 'print(__import__("my_module").MyClass.__doc__)')
Private instance attribute: size
"""

class Square:
    def __init__(self, size=0):
        if size != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

    def area(self):
        ar = self.__size * self.__size
        return ar

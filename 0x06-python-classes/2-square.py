#!/usr/bin/python3

"""class: Square

python3 -c 'print(__import__("my_module").MyClass.__doc__)')
Private instance attribute: size

"""
class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError
        elif size < 0:
            raise ValueError
        
        self.__size = size

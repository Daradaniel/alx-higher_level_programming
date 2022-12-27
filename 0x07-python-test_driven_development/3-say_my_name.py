#!/usr/bin/python3

"say_my_name module"

def say_my_name(first_name, last_name=""):

    """
    :param
    first_name: first name
    :param
    last_name: last nme
    :return:
    "My name is <first_name> <last_name>
    """

    result = ""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    result = print("My name is {:s} {:s}".format (first_name, last_name))
    return result

#!/usr/bin/python3

""" text_indentation module """

def text_indentation(text):
    """

    :param
    text:
    :return:
    text with two line space after ".", "?", and ":"

    """
    if type(text) != str:
        raise TypeError("text must be a string")

    delims = ".?:"
    nen = ""
    for k in text:
        nen += k
        if k in delims:
            print(nen.strip())
            print()
            nen = ""
    print(nen.strip(), end="")

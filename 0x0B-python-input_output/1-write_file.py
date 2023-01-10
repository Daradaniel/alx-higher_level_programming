#!/usr/bin/python3

def write_file(filename="", text=""):
    with open(filename) as f:
        text = f.__str__
        for str in text:
            count += 1

    return count

#!/usr/bin/python3
""" module: append to a file """

def append_write(filename="", text=""):
    """ append text to file  and return characters added"""
    if file == "":
        return 0
    with open(file, "a+") as f:
        return f.write(text)    

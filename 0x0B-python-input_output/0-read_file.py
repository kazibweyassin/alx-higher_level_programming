#!/usr/bin/python3
""" module: reads file """


def read_file(filename=""):
    """ read a file and print it out """
    if filename == "":
        return
    with open(file, "r") as f:
        for line in f:
            print(line, end="")

#!/usr/bin/python3
"""0-square

Define a square

"""

class Square:
    """A square

    represent a square
    """

    _size = None

    def __init__(self,size=0):
        """init method

        initialize a square

        args:
        size (int): the size of the square

        """

        self.__size = size

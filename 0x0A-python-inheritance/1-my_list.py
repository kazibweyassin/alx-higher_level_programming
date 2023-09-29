#!/usr/bin/python3
""" Create Mylist from list"""

class MyList(list):
    """MyList class which inherits from list"""

    def print_sorted(self):
        """ print the sorted list """
        print(sorted(self))

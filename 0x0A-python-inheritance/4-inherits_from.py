#!/usr/bin/python3
"""Only sub class of"""

def inherits_from(obj, a_class):
    """ Return true if and ony if obj is an instance"""
    if issubclass(type(obj), a_class) and(obj) is not a_class:
        return True
    return False

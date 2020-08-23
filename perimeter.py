#!/usr/bin/python3

def polygon(k, sides):
    if (k * sides) >= 1:
        return False
    else:
        return (1 - (k * sides))

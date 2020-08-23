#!/usr/bin/python3

from math import tan, pi

def polygon(perimeter, sides):
    area = sides * ((perimeter / sides) ** 2)
    area /= (4 * tan(pi / sides))
    return area

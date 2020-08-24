#!/usr/bin/python3

from math import tan, pi

def area(perimeter, sides):
    area = sides * ((perimeter / sides) ** 2)
    area /= (4 * tan(pi / sides))
    return area

def perimeter(k, sides):
    if (k * sides) >= 1:
        return 0
    else:
        return (1 - (k * sides))

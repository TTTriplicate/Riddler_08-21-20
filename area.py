#!/usr/bin/python3

def rect(perimeter):
    side = perimeter/4
    area = side ** 2
    return area

def tri(perimeter):
    area = 3**(1/2)
    side = perimeter/3
    area = area * ((side**2)/4)
    return area

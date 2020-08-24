#!/usr/bin/python3

from math import tan, pi

def area(perimeter, sides):
    '''
Calculates the maximum area of a polygon with a given perimeter and
number of sides.  Since the maximum area will be had in the case of a 
equilateral polygon, this formula can be used as a universal pattern
    '''
    area = sides * ((perimeter / sides) ** 2)
    area /= (4 * tan(pi / sides))
    return area

def perimeter(k, sides):
    '''
Based on the weighted value k and the number of sides, calculates
the side length of an equilateral polygon with the given number
of sides
    '''
    if (k * sides) >= 1:
        return 0
    else:
        return (1 - (k * sides))

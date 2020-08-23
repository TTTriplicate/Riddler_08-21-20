#!/usr/bin/python3

import sys
import area, perimeter #

k = [.2, .000001]
equalAt = -1
if len(sys.argv) < 2:#default case, find where 4 posts beats 3
    while equalAt == -1:
        nextGuess = (k[0] + k[1])/2
        print(nextGuess)
        #input()
        perimeters = (perimeter.polygon(nextGuess, 3), perimeter.polygon(nextGuess, 4))
        areas = (area.polygon(perimeters[0], 3), area.polygon(perimeters[1], 4))
        if areas[0] - areas[1] < .00001 and areas[0] - areas[1] > -.00001:
            equalAt = nextGuess
        elif areas[0] > areas[1]:
            k[0] = nextGuess
        else:
            k[1] = nextGuess

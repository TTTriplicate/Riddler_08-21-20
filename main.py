#!/usr/bin/python3

import sys
import area, perimeter #

k = [.2, .000000001]
if len(sys.argv) < 2:#default case, find where 4 posts beats 3
    rounds = 1
elif len(sys.argv) == 2:
    rounds = int(sys.argv[1]) + 3
else:
    print("Please provide 0 or 1 arguments, the number of posts up to which you want to find values of k.")

for i in range(3, 3 + rounds):
    print("i =", i)
    equalAt = -1
    while equalAt == -1:
        nextGuess = (k[0] + k[1])/2
        print(nextGuess)
        input()
        perimeters = (perimeter.polygon(nextGuess, i), perimeter.polygon(nextGuess, i+1))
        areas = (area.polygon(perimeters[0], i), area.polygon(perimeters[1], i+1))
        if areas[0] - areas[1] < .00001 and areas[0] - areas[1] > -.00001:
            equalAt = nextGuess
            k[1] = .2
        elif areas[0] > areas[1]:
            k[0] = nextGuess
        elif areas[0] < areas[1]:
            k[1] = nextGuess
    print(i+1, "Provides a greater area than", i, "sides for k smaller than", equalAt)

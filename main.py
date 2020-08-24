#!/usr/bin/python3

import sys
import polygon #

if len(sys.argv) < 2:#default case, find where 4 posts beats 3
    num = 1
elif len(sys.argv) == 2:
    num = int(sys.argv[1])
else:
    print("Please provide 0 or 1 arguments, the number of posts up to which you want to find values of k.")

k = [.2, .000000001]
for i in range(3, num):
    #print("i =", i)
    equalAt = -1
    while equalAt == -1:
        nextGuess = (k[0] + k[1])/2
        #print(nextGuess)
        #input()
        perimeters = (polygon.perimeter(nextGuess, i), polygon.perimeter(nextGuess, i+1))
        areas = (polygon.area(perimeters[0], i), polygon.area(perimeters[1], i+1))
        if areas[0] - areas[1] < .00000001 and areas[0] - areas[1] > -.00000001:
            equalAt = nextGuess
            k[1] = .00000000
        elif areas[0] > areas[1]:
            k[0] = nextGuess
        elif areas[0] < areas[1]:
            k[1] = nextGuess
    print(i+1, "Provides a greater area than", i, "sides for k smaller than", equalAt)

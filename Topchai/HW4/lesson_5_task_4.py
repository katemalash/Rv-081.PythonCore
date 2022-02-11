'''
Is possible to place a round stage with radius R in a square hall of square 
S so that there is a passage was at least K from the wall to the stage?
'''

import math


print("\nThis program determine if possible to place a round stage to the square hall with specific parameters so there was enough space for specific passage.\n")

roundStageRadius = int(input("Please enter the radius of round stage: "))
squareHallArea = int(input("Please enter the area of square hall: "))
passageSize = int(input("Please enter the size of passage you need: "))

squareSide = math.sqrt(squareHallArea)
stageDiametr = roundStageRadius*2
availableRoom = squareSide - stageDiametr


print(f"\nBased on the entered parameters, the side of the squre is equal to {squareSide} and the stage diametr is {stageDiametr}.")

if (squareSide - stageDiametr) >= passageSize:
    print(f"\nThe distance to the wall will be {availableRoom} meters, so yes, you have enough space for passage.\n")

else:
    neededStageRadius = (squareSide - passageSize)/2
    print(f"\nUnfortunately, you have not enough space for passage with such stage. For this hall, you need the stage with radius {neededStageRadius}.\n")

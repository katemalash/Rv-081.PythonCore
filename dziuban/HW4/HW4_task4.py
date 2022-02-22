import math

square_hall = int(input("Enter the square area: "))
radius_stage = int(input("Enter the radius: "))
K = int(input("Enter K: "))

side_hall = math.sqrt(square_hall)

if side_hall - radius_stage*2 > K:
    print("It is possible")
else:
    print("It is impossible")
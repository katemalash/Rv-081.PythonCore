import math


round_stage = int(input("Enter radius of the stage"))
square_hall = math.sqrt(int(input("Enter square of the hall")))
passage = int(input("Enter the passage between stage and wall"))
R = round_stage*2

if square_hall - R > passage:
    print("Yes it's possible to place it")
else:
    print("No, it's not possible")
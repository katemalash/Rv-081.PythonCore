'''
The number of a place in the reserved carriage is given. Determine 
which place it is: top or bottom, compartment or side.
'''

while True:
    try:
        placeNumber = int(input("\nPlease enter the seat number from 1 to 54 >>> "))

    except ValueError:
        print("\nSorry, I didn't understand that.")
        continue

    if placeNumber < 1:
        print("\nSorry, the seat number must not be less than 1.")
        continue

    elif placeNumber > 54:
        print("\nSorry, the seat number must not be greater than 54.")

    else:
        break

if placeNumber // 2 == 0:
    seat = "top seat"

else:
    seat = "bottom seat"

if 36 > placeNumber > 0:
    seatSide = "compartment place"

elif 54 > placeNumber > 36:
    seatSide = "side place"

print(f"\nYou have a {seat}, and it's a {seatSide}.\n")
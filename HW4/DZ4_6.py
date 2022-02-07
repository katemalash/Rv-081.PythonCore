user_place = int(input("Enter your seat number: "))

if user_place >= 1 and user_place <= 54:
    if user_place % 2 == 0 and user_place <= 36:
        print("Top compartment")
    elif user_place % 2 == 1 and user_place <= 36:
        print("Bottom compartment")
    else:
        print("Bottom side")
else:
    print("Don`t have place")
place = int(input("Enter the place number you want to choose: "))

if 1 <= place <= 36 and place % 2 == 0:
    print("Top place in compartment")

elif 1 <= place <= 36 and place % 2 != 0:
    print("Bottom place in compartment")

elif 37 <= place <= 54 and place % 2 == 0:
    print("Top place on the side")

elif 37 <= place <= 54 and place % 2 != 0:
    print("Bottom place on the side")

else:
    print("Such place doesn't exist")
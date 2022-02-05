user_number = int(input("Enter number: "))

if user_number >= 0:
    if user_number < 10:
        print("positive one-digit")
    elif user_number >= 10 and user_number < 100:
        print("positive two-digit")
    else:
        print("positive three or more digit number")
else:
    if user_number > -10:
        print("negative one-digit")
    elif user_number <= -10 and user_number > -100:
        print("negative two-digit")
    else:
        print("negative three or more digit number")
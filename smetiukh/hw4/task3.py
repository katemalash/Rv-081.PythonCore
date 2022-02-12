number = int(input("Enter the digit"))

if number > 100:
    print("Positive three-digit")
elif number >= 10:
    print("Positve two-digit")
elif number > 0:
    print("Positive one-digit")
elif number <= -100:
    print("Negative three-digit")
elif number <= -10:
    print("Negative two-digit")
elif number < 0:
    print("Negative one-digit")
elif number == 0:
    print("Zero")

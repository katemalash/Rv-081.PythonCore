tuple_all = ("a", "d", 61, 21, 1, "@", "#", "$", "a", "1")

user_simvol = input("Enter your simvol: ")

if user_simvol.isdigit() == True:
    print("It is number or string?")
    ansver = input("Enter n or s :")
    if ansver == "n":
        user_simvol = int(user_simvol)

print(tuple_all.index(user_simvol))
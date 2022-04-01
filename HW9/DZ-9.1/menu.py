from Fish import *
from Pound import *


print("1. View capacity \n2. View state of Pond \n3. Add fish \n4. Catch fish "
      "\n5. Create new fish  \n6. Finish the game")

user = Pound()
fish1 = UserFish("Som", 111, 111)
listFish = [fish1]

while True:
    inputUser = int(input(">>"))

    if inputUser == 1:
        user.show_capacity()

    elif inputUser == 2:
        user.show_state()

    elif inputUser == 3:
        inputFish = input("Carp or Sea fish or your? ")
        if inputFish == "Carp":
            inputFish = Carp()
            user.obtain_fish(inputFish)
        elif inputFish == "Sea fish":
            inputFish = SeaFish()
            user.obtain_fish(inputFish)
        elif inputFish == "my":
            try:
                print(listFish)
                choice = int(input("Enter number fish: "))
                user.obtain_fish(listFish[choice-1])
                listFish.pop(choice-1)
            except NameError:
                print("You haven't created your fish , please press 5")
            except IndexError:
                print("No such fish")
            except ValueError:
                print("Invalid input")

    elif inputUser == 4:
        user.show_capacity()
        inputFish = int(input("Enter number: "))
        user.lost_fish(inputFish-1)

    elif inputUser == 5:
        name = input("Name your fish: ")
        size = input("Size your fish: ")
        weight = input("Weight your fish: ")
        userFish = UserFish(name, size, weight)
        listFish.append(userFish)

    elif inputUser == 6:
        print("End this game")
        break

    else:
        print(f"This game doesn't have point number {inputUser}")

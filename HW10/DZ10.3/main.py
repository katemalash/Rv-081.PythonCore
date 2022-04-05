from Fish import *
from Pound import *
from my_error import *

print("1. View capacity \n2. View state of Pond \n3. Add fish \n4. Catch fish "
      "\n5. Create new fish  \n6. Finish the game")

user = Pound()
fish1 = UserFish("CatFish", 111, 111)
listFish = [fish1]
inputUser = None

while True:
    try:
        inputUser = int(input(">>"))
        if inputUser not in (1, 2, 3, 4, 5, 6):
            raise MyError("There is no such item in the menu")
    except MyError as f:
        print("MenuError:", f.data)
        print("Please enter menu item")
    except ValueError:
        print("Enter number menu")

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
        else:
            print("You didn't make a choice \nTry again")

    elif inputUser == 4:
        user.show_capacity()
        try:
            inputFish = int(input("Enter number: "))
            user.lost_fish(inputFish-1)
        except IndexError:
            print("You don't have this fish")
        except ValueError:
            print("Invalid input")

    elif inputUser == 5:
        name = input("Name your fish: ")
        size = input("Size your fish: ")
        weight = input("Weight your fish: ")
        userFish = UserFish(name, size, weight)
        listFish.append(userFish)

    elif inputUser == 6:
        print("End this game")
        break

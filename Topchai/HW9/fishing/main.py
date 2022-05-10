import os
from fish import *
from pond import *
from messages import *


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def quit():
    "Finish the game."

    print(Messages.finishedMenu)

    pondCall.showCapacity()
    print(pondCall.showState())

    print(Messages.lineMenu)

    exit()


pondCall = Pond()
fishCall = Fish()

addedFishList = []

cls()
print(Messages.starGameMenu)

action1 = ""

while action1 != 1:
    try:
        action1 = int(input("> "))
        if action1 == 1:
            cls()
        elif action1 == 2:
            cls()
            print(Messages.starGameMenu)
            print("\nSee you!\n")
            exit()
        else:
            cls()
            print(Messages.starGameMenu)
            print("No such option. Please try again.")

    except ValueError:
        print("Wrong option, please try again.")

print(Messages.gameMenu)

# The main loop

while True:
    try:
        action2 = int(input("\nSelect an option from the menu: "))

        if action2 == 1:
            cls()
            print(Messages.gameMenu)

            addedFish = fishCall.addNewFish()
            addedFishList.append(addedFish)

            fishCall.showAvailableFish(addedFishList)

        elif action2 == 2:
            cls()
            print(Messages.gameMenu)

            fishCall.showAvailableFish(addedFishList)

        elif action2 == 3:

            if not addedFishList:
                fishCall.showAvailableFish(addedFishList)

                print(Messages.lineMenu)

                pondCall.showCapacity()

                print(Messages.lineMenu)
                print("There is no available fish.")
                print(Messages.lineMenu)

            else:
                cls()

                print(Messages.gameMenu)

                fishCall.showAvailableFish(addedFishList)

                print(Messages.lineMenu)
                pondCall.showCapacity()
                print(Messages.lineMenu)

                action3 = int(
                    input(
                        "\nSelect the fish you want to release to the pond: "))
                cls()

                print(Messages.gameMenu)

                pondCall.obtainFish(addedFishList, action3)
                fishCall.showAvailableFish(addedFishList)

                print(Messages.lineMenu)
                pondCall.showCapacity()
                print(Messages.lineMenu)

        elif action2 == 4:
            cls()

            print(Messages.gameMenu)

            pondCall.showCapacity()

        elif action2 == 5:
            cls()

            print(Messages.gameMenu)

            print(pondCall.showState())

        elif action2 == 6:
            cls()

            print(Messages.gameMenu)

            if not pondCall.capacityP:
                fishCall.showAvailableFish(addedFishList)
                print(Messages.lineMenu)
                pondCall.showCapacity()
                print(Messages.lineMenu)

                print("There is no fish in the Pond.")

                print(Messages.lineMenu)

            else:
                pondCall.catchFish(addedFishList)
                fishCall.showAvailableFish(addedFishList)

                print(Messages.lineMenu)

                pondCall.showCapacity()

                print(Messages.lineMenu)

        elif action2 == 7:
            cls()

            print(Messages.gameMenu)

            fishCall.showAvailableFish(addedFishList)

            name = input("\nName: ")
            weight = input("Weight: ")
            color = input("Color: ")
            userFish = UserFish(name, weight, color)
            cls()
            addedFishList.append(userFish)

            print(Messages.gameMenu)

            fishCall.showAvailableFish(addedFishList)

        elif action2 == 8:
            cls()

            print(Messages.gameMenu)

        elif action2 == 9:
            cls()
            quit()

        else:
            cls()

            print(Messages.gameMenu)

            print("No such option. Please try again.")
    except ValueError:
        print("\nWrong option, please try again.")

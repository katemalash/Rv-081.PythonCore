from random import randint


class Fish(object):
    weight = 5

    def addNewFish(self):
        rd = randint(1, 3)
        if rd == 1:
            colors = ("Grey", "Black", "White")
            color = colors[randint(0, 2)]
            return SheatFish(randint(1, 15), color, randint(1, 10))

        elif rd == 2:
            colors = ("White", "Grey", "Marin")
            color = colors[randint(0, 2)]
            return Salmon(randint(1, 10), color)

        else:
            colors = ("Blue", "Black", "Green")
            color = colors[randint(0, 2)]
            return Carp(randint(1, 15), color)

    def showAvailableFish(self, arg):
        """This function shows the available fish."""

        print(f"Available fish: {len(arg)}\nList of available fish:\n")
        for i in arg:
            print(f"{arg.index(i) + 1}. {i}")


class SheatFish(Fish):
    whisckerLenght = 0

    def __init__(self, weight, color, whisckerLenght):
        self.weight = weight
        self.color = color
        self.whisckerLenght = whisckerLenght

    def __str__(self):
        return f"Sheatfish: Weight - {self.weight}kg, Color - {self.color}, Whisker lenght - {self.whisckerLenght}sm"


class Carp(Fish):
    color = ""

    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def __str__(self):
        return f"Carp:      Weight - {self.weight}kg, Color - {self.color}"


class Salmon(Fish):
    color = "Blue"

    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def __str__(self):
        return f"Salmon:    Weight - {self.weight}kg, Color - {self.color}"


class UserFish(Fish):
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def __repr__(self):
        return f"{self.name}:   Weight - {self.weight}kg, Color - {self.color}"

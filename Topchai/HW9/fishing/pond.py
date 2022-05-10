from random import randint


class Pond(object):
    def __init__(self):
        self.capacityP = []
        self.state = "Empty"

    def showState(self):
        """This function shows the state of the pond"""

        if len(self.capacityP) < 1:
            self.state = "Empty"
        elif len(self.capacityP) < 5:
            self.state = "Poor"
        elif len(self.capacityP) <= 10:
            self.state = "Normal"
        elif len(self.capacityP) > 10:
            self.state = "Rich"

        return f"The pond state is: {self.state}"

    def showCapacity(self):
        """This function shows the capacityP of the pond."""

        print(
            f"Available fish in the pond: {len(self.capacityP)}\nList of fish in the pond:\n")
        for i in self.capacityP:
            print(f"{self.capacityP.index(i) + 1}. {i}")

    def obtainFish(self, arg, index):
        """Adding the fish to the pond."""

        return self.capacityP.append(arg.pop(index-1))

    def catchFish(self, arg):
        """Function to catch the fish."""

        randIndex = randint(0, (len(self.capacityP)-1))

        return arg.append(self.capacityP.pop(randIndex))

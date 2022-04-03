class Fish(object):
    weight = 10


class SeaFish(Fish):
    whiskerLength = 100

    def __repr__(self):
        return SeaFish.__name__


class Carp(Fish):
    color = "gray"

    def __repr__(self):
        return Carp.__name__


class UserFish(Fish):
    def __init__(self, name, size, weight):
        self.name = name
        self.size = size
        self.weight = weight

    def __repr__(self):
        return self.name



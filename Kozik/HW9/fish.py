class Fish:

    def __init__(self, weight):
        self.weight = weight


class Catfish(Fish):

    def __init__(self, weight, length):
        Fish.__init__(self, weight)
        self.length_of_whisker = length

    def __repr__(self):
        return 'catfish'


class Carp(Fish):

    def __init__(self, weight, color):
        Fish.__init__(self, weight)
        self.color = color

    def __repr__(self):
        return 'carp'

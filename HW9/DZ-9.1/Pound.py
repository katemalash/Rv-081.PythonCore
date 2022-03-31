class Pound(object):
    capacity = list()

    def state(self):
        if len(self.capacity) < 5:
            return "poor"
        elif len(self.capacity) <= 10:
            return "normal"
        else:
            return "rich"

    def obtain_fish(self, fish):
        return self.capacity.append(fish)

    def lost_fish(self, fish):
        return self.capacity.pop(fish)

    def show_capacity(self):
        return print(self.capacity)

    def show_state(self):
        return print(self.state())

class Pond:

    capacity = []
    state = 'Poor'

    def __update_state(self, capacity):
        self.state = 'Rich' if len(capacity) > 10 else \
            ('Poor' if len(self.capacity) < 5 else 'Normal')

    def obtain_fish(self, fish):
        self.capacity.append(fish)
        self.__update_state(self.capacity)

    def lost_fish(self, fish):
        if fish in self.capacity:
            self.capacity.remove(fish)
            self.__update_state(self.capacity)

    def show_capacity(self):
        if len(self.capacity) == 0:
            print('Not Found\n')
        else:

            for fish in self.capacity:
                print(str(fish))
            else:
                print()

    def show_state(self):
        print(self.state)
        print()

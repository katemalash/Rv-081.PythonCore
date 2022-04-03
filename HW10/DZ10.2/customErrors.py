class LikeError(Exception):
    def __init__(self, data, user_number):
        self.data = data
        self.user_number = user_number

    def __str__(self):
        return repr(self.data)


class ZeroError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)

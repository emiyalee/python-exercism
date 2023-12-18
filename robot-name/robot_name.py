import string
from secrets import choice


class Robot:
    def __init__(self):
        self.name = ""
        self.reset()

    def reset(self):
        prefix = ''.join(choice(string.ascii_uppercase) for i in range(2))
        suffix = ''.join(choice(string.digits) for i in range(3))
        self.name = prefix + suffix

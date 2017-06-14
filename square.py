import constants


class Square:

    def __init__(self, position):
        self.position = position
        self.unmark()

    def __str__(self):
        return self.char

    def mark_as_missed(self):
        self.char = '~'
        self.was_shot = True

    def mark_as_mast(self):
        self.char = 'S'

    def mark_as_hit(self):
        self.char = 'X'
        self.was_shot = True

    def mark_as_submerged(self):
        self.char = '#'

    def unmark(self):
        self.char = ' '
        self.was_shot = False

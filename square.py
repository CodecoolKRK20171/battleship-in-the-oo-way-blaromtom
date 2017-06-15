import constants


class Square:

    def __init__(self, position, ocean):
        self.ocean = ocean
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

    def get_neighbour_squares(self, distance=1):
        neighbours = []
        x, y = self.position
        for delta_y in range(-distance, distance + 1):
            for delta_x in range(-distance, distance + 1):
                if Square.is_on_board((x+delta_x, y+delta_y)):
                    neighbours.append(self.ocean.board[y + delta_y][x + delta_x])
        return neighbours

    @staticmethod
    def is_on_board(position):
        x, y = position
        if y in range(constants.HEIGHT) and x in range(constants.WIDTH):
            return True
        else:
            return False

# import string
from ship import Ship
from square import Square
import constants

class Ocean:

    def __init__(self):
        self.board = [[Square((x, y)) for x in range(constants.WIDTH)] for y in range(constants.HEIGHT)]

    def print_board(self, show_hide=False):
        margin_size = 2
        header_row = ' ' * margin_size + '|' + ' '.join(sorted(list(constants.COLLUMNS_NAME_INDEX)))
        dividing_line = '-' * margin_size + '|' + '-'.join(['-' for i in range(constants.WIDTH)])
        other_rows = ''
        for y in range(constants.HEIGHT):
            if show_hide:
                line = [square.__str__() for square in self.board[y]]
            else:
                line = [square.__str__() if square.was_shot else ' ' for square in self.board[y]]
            other_rows += '{0:>{margin}}|{1}'.format(y + 1, ' '.join(line), margin=margin_size) + '\n'

        print(header_row + '\n' + dividing_line + '\n' + other_rows)

    def clear_board(self):
        for line in self.board:
            for square in line:
                square.unmark()

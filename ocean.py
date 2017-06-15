# import string
from ship import *
from square import *
from UI import *
import constants


class Ocean:
    '''
    Class of ocean objects

    Attributes:
    -----------
    board - list of lists of Square obj
    ships - list of Ship obj
    '''

    def __init__(self):
        '''
        Object creator.
        Creates board of height and width prewritten in constans module, and fills it with Square obj
        Runs place_ship() method
        '''
        self.board = [[Square((x, y), self) for x in range(constants.WIDTH)] for y in range(constants.HEIGHT)]
        self.place_ships()

    def print_board(self, show_hide=False):
        '''
        Method to print objects board with headers (taken from constants module).
        if show_hide is set to True, method prints whitespaces istead of Square obj which haven't been shot before

        Arguments:
        ----------
        show_hide - bool, default False
        '''
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
        '''
        Method to unmark all Square objects from object's board
        '''
        for line in self.board:
            for square in line:
                square.unmark()

    def place_ships(self):
        '''
        Method to place ships from list imported from constants module
        '''
        self.ships = []
        available_ships = sorted([ship for ship in constants.SHIPS_TO_PLACE if ship not in self.ships])
        while available_ships:
            print('Place your ships in the ocean:\n')
            self.print_board(show_hide=True)
            ship_type = choose_ship(available_ships)
            self.make_ship(ship_type)
            available_ships.remove(ship_type)
        print('All ships placed\n')
        self.print_board(show_hide=True)
        end = get_confirmation('Press Y to confirm: ')
        if end:
            for line in self.board:
                for square in line:
                    if square.char == '~':
                        square.unmark()
        else:
            for ship in self.ships:
                self.remove_ship(ship)
            self.clear_board()
            self.place_ships()

    def make_ship(self, ship_type):
        '''
        Method to create Ship object of given type, and add it to list

        Arguments:
        ----------
        ship_type - str
        '''
        print('Making {}:\n'.format(ship_type))
        laying = set_ship_laying()
        if laying == 'curved':
            ship_squares = Ship.form_curved_ship(self, ship_type)
        else:
            ship_squares = Ship.form_straight_ship(self, ship_type, laying)
        for square in ship_squares:
            for neighbour_square in square.get_neighbour_squares():
                if neighbour_square not in ship_squares:
                    neighbour_square.mark_as_missed()
            square.mark_as_mast()
        self.ships.append(Ship(self, ship_squares, ship_type))

    def remove_ship(self, ship):
        '''
        Method to remove Ship obj from list

        Arguments:
        ----------
        ship - Ship obj
        '''
        for square in ship.squares:
            square.unmark()
        self.ships.remove(ship)

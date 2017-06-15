import constants
from square import *
from UI import *


class Ship:
    '''
    class of Ship objects

    Attributes:
    -----------
    ocean - Ocean obj
    squares = list of Square obj
    is_submerged = bool
    ship_type = str
    '''

    def __init__(self, ocean, squares, ship_type):
        self.ocean = ocean
        self.squares = squares
        self.is_submerged = False
        self.ship_type = ship_type

    def receive_hit(self, position):
        '''
        Method to react on hit in given position

        Arguments:
        ----------
        position - tuple (int, int)
        '''
        if not self.is_submerged:
            for square in self.squares:
                if square.position == position:
                    square.mark_as_hit()
            if all([square.was_shot for square in self.squares]):
                self.become_submerged()

    def become_submerged(self):
        '''
        Method to change slef attribute is_submerged and mark it on ocean
        '''
        self.is_submerged = True
        for square in self.squares:
            square.mark_as_submerged()
            for neighbour_square in square.get_neighbour_squares():
                if neighbour_square not in self.squares:
                    neighbour_square.mark_as_missed()

    @staticmethod
    def form_straight_ship(ocean, ship_type, laying):
        '''
        Static method of class Ship.
        Used to get Squares objects of straight ship of given type from given ocean

        Arguments:
        ----------
        ocean - Ocean obj
        ship_type - str
        laying - str

        Return:
        list of Square obj
        '''
        build_direction = 'right' if laying == 'horizontal' else 'down'
        print("Select first position. The ship will continue building itself {} from this position.".format(build_direction))
        try:
            x, y = get_coordinate('Choose position: ')
            ship_squares = []
            if ocean.board[y][x].char == ' ':
                for i in range(constants.SHIPS_TO_PLACE[ship_type]):
                    if laying == 'horizontal' and ocean.board[y][x + i].char == ' ':
                            ship_squares.append(ocean.board[y][x + i])
                    elif laying == 'vertical' and ocean.board[y + i][x].char == ' ':
                            ship_squares.append(ocean.board[y + i][x])
                    else:
                        raise IndexError
            else:
                raise IndexError
        except IndexError:
            print('Not enough place for that ship, try again!')
            ship_squares = Ship.form_straight_ship(ocean, ship_type, laying)
        return ship_squares

    @staticmethod
    def form_curved_ship(ocean, ship_type):
        '''
        Static method of class Ship.
        Used to get Squares objects of curved ship of given type from given ocean

        Arguments:
        ----------
        ocean - Ocean obj
        ship_type - str

        Return:
        list of Square obj
        '''
        ship_squares = []
        try:
            while len(ship_squares) < constants.SHIPS_TO_PLACE[ship_type]:
                print(len(ship_squares))
                x, y = get_coordinate("Choose {} position: ".format(len(ship_squares) + 1))
                if ocean.board[y][x].char != ' ':
                    print('This position is already occupied!')
                elif len(ship_squares) == 0:
                    ship_squares.append(ocean.board[y][x])
                elif ocean.board[y][x] in ship_squares:
                    print('Already added!')
                elif any([neighbour in ship_squares for neighbour in ocean.board[y][x].get_neighbour_squares()]):
                    ship_squares.append(ocean.board[y][x])
                else:
                    print('Not connected to other parts of ship')
        except IndexError:
            print('Not enough place for that ship, try again!')
            ship_squares = Ship.form_curved_ship(ocean, ship_type)
        return ship_squares

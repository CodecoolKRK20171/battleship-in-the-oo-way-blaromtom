import constants
from square import Square

class Ship:

    def __init__(self, ocean, ship_type):
        self.ocean = ocean
        self.squares = []
        self.is_submerged = False
        self.ship_type = ship_type
        self.set_positions()
        self.get_ocean_squares()


    def set_laying(self):
        while True:
            self.is_straight = True               # temporary solution
            choose = input("\nEnter 'V', 'H', 'C' to place ship vertically, horizontally or curved: ")
            if choose.lower() == 'v':
                self.is_horizontal = False
                break
            elif choose.lower() == 'h':
                self.is_horizontal = True
                break
            elif choose.lower() == 'c':     # temporary solution
                self.is_straight = False    # temporary solution
                break                       # temporary solution
            else:
                print('Wrong choose')


    def set_positions(self):
        self.set_laying()

        if self.is_straight:
            build_direction = 'right' if self.is_horizontal else 'down'
            print("Select first position. The ship will continue building itself {} from this position.".format(build_direction))
            try:
                x, y = get_coordinate("Choose position: ")
                self.positions = []
                if self.ocean.board[y][x].char == ' ':
                    for i in range(constants.SHIPS_TO_PLACE[self.ship_type]):
                        if self.is_horizontal:
                            if self.ocean.board[y][x + i].char == ' ':
                                self.positions.append((x + i, y))
                            else:
                                raise IndexError
                        else:
                            if self.ocean.board[y + i][x].char == ' ':
                                self.positions.append((x, y + i))
                            else:
                                raise IndexError
                    for square in self.get_neighbour_squares():
                        square.mark_as_missed()
                else:
                    raise IndexError
            except IndexError:
                print('Not enough place for that ship, try again!')
                self.set_positions()

        else:       # curved ship
            self.place_curved()


    def place_curved(self):
        '''
        Builds curved ship list.
        '''
        self.positions = []

        try:
            for i in range(constants.SHIPS_TO_PLACE[self.ship_type]):
                x, y = get_coordinate("Choose " + str(i+1) + " position: ")

                if self.ocean.board[y][x].char != ' ':
                    raise IndexError
                else:
                    self.positions.append((x, y))

        except IndexError:
            print('Not enough place for that ship, try again!')
            self.place_curved()
        else:
            print(self.positions)
            self.check_shape(self.positions)  # raises value if failed


    def check_shape(self, positions):
        '''
        Checks connection between a new and old parts of the ship.
        Raises ValueError in case wrong position of the new part.
        Arguments:
        x coordinate    - int
        y coordinate    - int
        '''

        for i in range(len(self.positions)):
            orphaned_part = True
            x = self.positions[i][0]
            y = self.positions[i][1]
            for j in range(len(self.positions)):
                if ( i != j ) and (\
                    ( x == self.positions[j][0]  and ( y-1 == self.positions[j][1] or y+1 == self.positions[j][1] ) ) or\
                    ( y == self.positions[j][1]  and ( x-1 == self.positions[j][0] or x+1 == self.positions[j][0] ) ) ):
                    orphaned_part = False
        if orphaned_part:
            print('Wrong shape of the ship! Try again!')
            self.set_positions()


    def get_ocean_squares(self):
        '''Method used to make list of Square objects (parts of Ocean) which will be part of ship'''
        for x, y in self.positions:
            self.squares.append(self.ocean.board[y][x])
        for square in self.squares:
            square.mark_as_mast()

    def get_neighbour_squares(self):
        neighbour_positions = []
        neighbour_squares = []
        for x, y in self.positions:
            for delta_y in range(-1, 2):
                for delta_x in range(-1, 2):
                    if y + delta_y in range(constants.HEIGHT) and x + delta_x in range(constants.WIDTH):
                        if (x + delta_x, y + delta_y) not in neighbour_positions and (x + delta_x, y + delta_y) not in self.positions:
                            neighbour_positions.append((x + delta_x, y + delta_y))
        for line in self.ocean.board:
            for square in line:
                if square.position in neighbour_positions:
                    neighbour_squares.append(square)

        return neighbour_squares

    def receive_hit(self, position):
        if not self.is_submerged:
            for square in self.squares:
                if square.position == position:
                    square.mark_as_hit()
            if all([square.was_shot for square in self.squares]):
                self.become_submerged()

    def become_submerged(self):
        self.is_submerged = True
        for square in self.squares:
            square.mark_as_submerged()
        for square in self.get_neighbour_squares():
            square.mark_as_missed()


def get_coordinate(input_text):
    while True:
        choose = input(input_text).upper()
        try:
            if len(choose) < 2:
                raise ValueError
            elif choose[0] not in constants.COLLUMNS_NAME_INDEX or int(choose[1:]) not in constants.COLLUMNS_NAME_INDEX.values():
                raise ValueError
        except (TypeError, ValueError):
            print('Wrong coordinate!')
        else:
            return constants.COLLUMNS_NAME_INDEX[choose[0]] - 1, int(choose[1:]) - 1

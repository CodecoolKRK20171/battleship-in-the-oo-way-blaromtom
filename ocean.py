import string


class Player:

    SHIPS_TO_PLACE = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}

    def __init__(self, name):
        self.name = name
        self.ocean = Ocean()
        self.place_ships()

    def place_ships(self):
        self.ships = []
        available_ships = sorted([ship for ship in Player.SHIPS_TO_PLACE if ship not in self.ships])
        while available_ships:
            print('Player: {}\n'.format(self.name))
            print('Place your ships in the ocean:\n')
            self.ocean.print_board(show_hide=True)
            print('\nAvailable ships:\n')
            print('\n'.join(['{0} - {1}'.format(i + 1, available_ships[i]) for i in range(len(available_ships))]))
            while True:
                try:
                    choose = int(input('\nEnter number to choose: '))
                    if choose - 1 in range(len(available_ships)):
                        ship_type = available_ships[choose - 1]
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print('Wrong choose!')
            print('Making {}:\n'.format(ship_type))
            self.ships.append(Ship(self.ocean, ship_type))
            available_ships.remove(ship_type)
        print('All ships placed\n')
        self.ocean.print_board(show_hide=True)
        end = input("Enter 'Y' to affirm placing: ")
        if end.upper() != 'Y':
            self.remove_ships()
            self.ocean.clear_board()
            self.place_ships()
        else:
            for line in self.ocean.board:
                for square in line:
                    if square.char == '~':
                        square.unmark()

    def remove_ships(self):
        for ship in self.ships:
            for square in ship.squares:
                square.unmark()
        self.ships = []

    def shoot(self):
        shoot = get_coordinate("Choose place to shoot: ")
        return shoot

    def handle_rivals_shoot(self, shoot):
        x, y = shoot
        hited_square = self.ocean.board[y][x]
        if not hited_square.was_shot:
            for ship in self.ships:
                if hited_square in ship.squares:
                    ship.receive_hit(shoot)
                    if ship.is_submerged:
                        return 'You hit, and destroyed {}.'.format(ship.ship_type)
                    else:
                        return 'You hit'
            else:
                self.ocean.board[y][x].mark_as_missed()
                return 'You missed'


class Ocean:
    HEIGHT = 10
    WIDTH = 10
    FILL_CHAR = ' '
    COLLUMNS_NAME_INDEX = {string.ascii_uppercase[i]: i + 1 for i in range(WIDTH)}

    def __init__(self):
        self.board = [[Square((x, y)) for x in range(Ocean.WIDTH)] for y in range(Ocean.HEIGHT)]

    def print_board(self, show_hide=False):
        margin_size = 2
        header_row = ' ' * margin_size + '|' + ' '.join(sorted(list(Ocean.COLLUMNS_NAME_INDEX)))
        dividing_line = '-' * margin_size + '|' + '-'.join(['-' for i in range(Ocean.WIDTH)])
        other_rows = ''
        for y in range(Ocean.HEIGHT):
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


class Ship:

    def __init__(self, ocean, ship_type):
        self.ocean = ocean
        self.squares = []
        self.is_submerged = False
        self.ship_type = ship_type
        self.set_positions()
        self.get_ocean_squares()

    def set_positions(self):
        self.set_laying()
        build_direction = 'right' if self.is_horizontal else 'down'
        print("Select first position. The ship will continue building itself {} from this position.".format(build_direction))

        try:
            x, y = get_coordinate("Choose position: ")
            self.positions = []
            if self.ocean.board[y][x].char == ' ':
                for i in range(Player.SHIPS_TO_PLACE[self.ship_type]):
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

    def set_laying(self):
        while True:
            choose = input("\nEnter 'V' to place ship vertically or 'H' to place it horizontally: ")
            if choose.lower() == 'v':
                self.is_horizontal = False
                break
            elif choose.lower() == 'h':
                self.is_horizontal = True
                break
            else:
                print('Wrong choose')

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
                    if y + delta_y in range(Ocean.HEIGHT) and x + delta_x in range(Ocean.WIDTH):
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
            elif choose[0] not in Ocean.COLLUMNS_NAME_INDEX or int(choose[1:]) not in Ocean.COLLUMNS_NAME_INDEX.values():
                raise ValueError
        except (TypeError, ValueError):
            print('Wrong coordinate!')
        else:
            return Ocean.COLLUMNS_NAME_INDEX[choose[0]] - 1, int(choose[1:]) - 1

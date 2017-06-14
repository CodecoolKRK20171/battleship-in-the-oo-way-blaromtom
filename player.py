import constants
from ocean import Ocean
from ship import Ship

class Player:

    def __init__(self, name):
        self.name = name
        self.ocean = Ocean()
        self.place_ships()


    def place_ships(self):
        self.ships = []
        available_ships = sorted([ship for ship in constants.SHIPS_TO_PLACE if ship not in self.ships])
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

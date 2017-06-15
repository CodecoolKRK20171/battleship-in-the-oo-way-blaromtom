import constants
from ocean import *
from ship import *
from UI import *


class Player:

    def __init__(self, name):
        self.name = name
        print('Player: {}\n'.format(self.name))
        self.ocean = Ocean()

    def shoot(self):
        shoot = get_coordinate("Choose place to shoot: ")
        return shoot

    def handle_rivals_shoot(self, shoot):
        x, y = shoot
        hited_square = self.ocean.board[y][x]
        if not hited_square.was_shot:
            for ship in self.ocean.ships:
                if hited_square in ship.squares:
                    ship.receive_hit(shoot)
                    if ship.is_submerged:
                        return 'You hit, and destroyed {}.'.format(ship.ship_type)
                    else:
                        return 'You hit'
            else:
                self.ocean.board[y][x].mark_as_missed()
                return 'You missed'

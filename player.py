import constants
from ocean import *
from ship import *
from UI import *


class Player:
    '''
    Class for Player objects

    Attributes:
    -----------
    name - str
    ocean - Ocean obj
    '''

    def __init__(self, name):
        self.name = name
        print('Player: {}\n'.format(self.name))
        self.ocean = Ocean()
        self.ocean.place_ships()

    def shoot(self):
        '''
        Method to choose coordinate player want to shoot

        Return:
        -------
        tuple (int, int)
        '''
        shoot = get_coordinate("Choose place to shoot: ")
        return shoot

    def handle_rivals_shoot(self, shoot):
        '''
        Method to response for rivals shoot into given position(shoot)

        Arguments:
        ----------
        shoot - tuple (int, int)

        Return:
        -------
        str
        '''
        x, y = shoot
        hited_square = self.ocean.board[y][x]
        if not hited_square.was_shot:
            for ship in self.ocean.ships:
                if hited_square in ship.squares:
                    ship.receive_hit(shoot)
                    if ship.is_submerged:
                        return 'Hit and destroyed: {}'.format(ship.ship_type)
                    else:
                        return 'Hit'
            else:
                self.ocean.board[y][x].mark_as_missed()
                return 'Missed'
        else:
            return 'You shot this place previusly'

    def handle_shot_result(self, result):
        print('\n{}'.format(result))

    def print_game_info(player):
        '''
        Function to print info about actual state of player and it's objects

        Parameters:
        -----------
        player - Player obj
        '''
        player.ocean.print_board(show_hide=False)
        print('\nLeft in battle: \n')
        for ship in player.ocean.ships:
            if not ship.is_submerged:
                print('{0} (lenght: {1} squares)'.format(ship.ship_type, constants.SHIPS_TO_PLACE[ship.ship_type]))
        print('\n')

import constants
import random
import time
from player import *
from ocean import *
from ship import *
from UI import *


class AI(Player):
    '''
    class for Artifician Inteligence player

    Attributes:
    -----------
    name - str
    ocean - Ocean obj
    rivals_ocean - Ocean obj
    expected_ship - list od Square obj
    previous_shots = list of Square obj
    '''

    def __init__(self):
        self.name = 'Computer'
        self.ocean = Ocean()
        self.ocean.place_random_ships()
        self.rivals_ocean = Ocean()
        self.expected_ship = []
        self.previous_shots = []

    def shoot(self):
        '''
        Method to choose random or consequent position of shoot

        Return:
        -------
        tuple (int, int)
        '''
        if self.expected_ship:
            shoot_option = []
            for square in self.expected_ship:
                neighbours = square.get_neighbour_squares()
                for neighbour in neighbours:
                    if neighbour not in self.expected_ship and not neighbour.was_shot:
                        shoot_option.append(neighbour)
            attack = random.choice(shoot_option)
            self.previous_shots.append(attack)
        else:
            while True:
                random_line = random.choice(self.rivals_ocean.board)
                if any([not square.was_shot for square in random_line]):
                    attack = random.choice([square for square in random_line if not square.was_shot])
                    self.previous_shots.append(attack)
                    break
        shot_position = attack.position
        print("Computer's shoot:", end=' ')
        time.sleep(2)
        print('{}{}'.format(constants.HEADER[shot_position[0]], shot_position[1] + 1))
        return shot_position

    def handle_shot_result(self, result):
        '''
        Method to handle and react to result of self previous shot

        Arguments:
        ----------
        result - str
        '''
        print('\n{}'.format(result))
        last_shoted_square = self.previous_shots[-1]
        if result == 'Missed':
            last_shoted_square.mark_as_missed()
        elif result == 'Hit':
            last_shoted_square.mark_as_hit()
            self.expected_ship.append(last_shoted_square)
        else:
            last_shoted_square.mark_as_hit()
            self.expected_ship.append(last_shoted_square)
            for square in self.expected_ship:
                square.mark_as_submerged()
                neighbours = square.get_neighbour_squares()
                for neighbour in neighbours:
                    if neighbour not in self.expected_ship:
                        neighbour.mark_as_missed()
            self.expected_ship = []

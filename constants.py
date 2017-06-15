'''
module with constant values needed in other modules
'''
import string

HEIGHT = 10
WIDTH = 10
FILL_CHAR = ' '
COLLUMNS_NAME_INDEX = {string.ascii_uppercase[i]: i + 1 for i in range(WIDTH)}
SHIPS_TO_PLACE = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}

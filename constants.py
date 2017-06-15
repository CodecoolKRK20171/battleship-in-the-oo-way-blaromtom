'''
module with constant values needed in other modules
'''
import string

HEIGHT = 10
WIDTH = 10
FILL_CHAR = ' '
HEADER = [string.ascii_uppercase[i] for i in range(WIDTH)]
COLLUMNS_NAME_INDEX = {HEADER[i]: i + 1 for i in range(len(HEADER))}
SHIPS_TO_PLACE = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
CREDITS = ['Tomasz Sowa', 'Błażej Pierzak', 'Mateusz Romanowski']

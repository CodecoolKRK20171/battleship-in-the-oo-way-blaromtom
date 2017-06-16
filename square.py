import constants


class Square:
    '''
    class of square obj - parts of Ocean and Ship objects

    Attributes:
    -----------
    ocean - Ocean obj
    position - tuple (int, int)
    char - str
    was_shot - bool
    '''

    def __init__(self, position, ocean):
        self.ocean = ocean
        self.position = position
        self.unmark()

    def __str__(self):
        return self.char

    def mark_as_missed(self):
        '''
        Method to mark obj on board as missed by changing char attribute
        '''
        self.char = '~'
        self.was_shot = True

    def mark_as_mast(self):
        '''
        Method to mark obj on board as mast of ship by changing char attribute
        '''
        self.char = 'S'

    def mark_as_hit(self):
        '''
        Method to mark obj on board as hit by changing char attribute
        '''
        self.char = 'X'
        self.was_shot = True

    def mark_as_submerged(self):
        '''
        Method to mark obj on board as suberged by changing char attribute
        '''
        self.char = '#'

    def unmark(self):
        '''
        Method to unmark obj on board as missed by changing char attribute
        '''
        self.char = ' '
        self.was_shot = False

    def get_neighbour_squares(self, distance=1, perpendicular=False):
        '''
        Method to get neighbour squares of self in given distance

        Arguments:
        ----------
        distance - int, default: 1

        Return:
        -------
        list of Square obj
        '''
        neighbours = []
        x, y = self.position
        if perpendicular:
            for delta_y in range(-distance, distance + 1):
                if Square.is_on_board((x, y+delta_y)) and (x, y+delta_y) != self.position:
                    neighbours.append(self.ocean.board[y + delta_y][x])
            for delta_x in range(-distance, distance + 1):
                if Square.is_on_board((x + delta_x, y)) and (x + delta_x, y) != self.position:
                    neighbours.append(self.ocean.board[y][x + delta_x])
        else:
            for delta_y in range(-distance, distance + 1):
                for delta_x in range(-distance, distance + 1):
                    if Square.is_on_board((x+delta_x, y+delta_y)):
                        neighbours.append(self.ocean.board[y + delta_y][x + delta_x])
        return neighbours

    @staticmethod
    def is_on_board(position):
        '''
        Static method to check if given position is in prewritten range of board height and width

        Arguments:
        ----------
        position - tuple (int, int)

        Return:
        -------
        bool
        '''
        x, y = position
        if y in range(constants.HEIGHT) and x in range(constants.WIDTH):
            return True
        else:
            return False

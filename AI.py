






class AI(Player):
    rivals_ocean = Ocean()

    previous_shots = []

    def attack(self):
        if self.expected_ship:
            [calc_neighbours for pos in self.expected_ship if pos]
            attack = random.choose([])

    attack = ()

    def get_response(self, effect):
        self.
        x, y = self.previous_shots[-1]
        if effect == 'You missed':
            rivals.ocean.board[y][x].mark_as_missed()
        elif effect == 'You hit':
            rivals.ocean.board[y][x].mark_as_hit()
            self.expected_ship.append((x, y))
        else:
            rivals_ocean.board[y][x].mark_as_hit()

            ship = [(x, y)]
            expanded_ship = []

            # while len(ship) != len(expanded_ship):
            #     for s_x, s_y in ship:
            #         expanded_ship = [(n_x, n_y) for n_x, n_y in calc_neighbours(s_x, s_y) if rivals_ocean.board[n_y][n_x].char == 'X' and (n_x, n_y) not in ship]
            #     ship = expanded_ship
            # for pos in ship:
            #     self.expected_ship.remove(pos)
            # rivals_ships.append(Ship(ship, rivals_ocean))
            # rivals_ships[-1].become_submerged()


def get_square(position, ocean):
    x, y = position
    return ocean.board[y][x]











def calc_neighbours(position, distance=1):
    """calculating and set to list all board cells in given distance (default 1) from x, y"""
    neighbours = []
    x, y = position
    for delta_y in range(-distance, distance + 1):
        for delta_x in range(-distance, distance + 1):
            if y + delta_y in range(33) and x + delta_x in range(106):
                neighbours.append((x + delta_x, y + delta_y))
    return neighbours

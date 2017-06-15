import sys
import time
import os
from player import *
import constants


def end_game(winner, loser):
    '''
    Function to print game sumary, and end program.

    Parameters:
    -----------
    winner - Player obj
    loser - Player obj
    '''
    print('\n'.join(read_file('game_over.txt')))
    print('\n{} wins!'.format(winner.name))
    time.sleep(3)
    for player in [winner, loser]:
        print('\n{}\n'.format(player.name))
        player.ocean.print_board(show_hide=True)
    sys.exit()


def read_file(file_name):
    '''
    Function to read txt file.

    Parameters:
    -----------
    file_name - str

    Return:
    -------
    list of string
    '''
    with open(file_name, 'r') as ascii_art:
        return [line[:-1] for line in ascii_art.readlines()]


def make_title_screen(title_file):
    '''
    Function to make title screen from title_file and credits

    Parameters:
    -----------
    title_file - str

    Return:
    -------
    str
    '''
    title_list = read_file(title_file)
    title = '\n'.join(title_list)
    width = len(title_list[1])
    credits = ['Tomasz Sowa', 'Błażej Pierzak', 'Mateusz Romanowski']

    for author in credits:
        title += '\n{:^{width}}'.format(author, width=width)

    return title + '\n'


def check_winner(players):
    '''
    Function to check if one of player is a winner, by checking if other one has lost all of his ships.
    If yes, runs end_game() Function

    Parameters:
    -----------
    players - list of Player obj
    '''
    for i in range(len(players)):
        if all([ship.is_submerged for ship in players[i].ocean.ships]):
            loser = players[i]
            players.remove(loser)
            winner = players[0]
            end_game(winner, loser)


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
            print('{0} (lenght: {1} sq  uares)'.format(ship.ship_type, constants.SHIPS_TO_PLACE[ship.ship_type]))
    print('\n')


def main():
    print(make_title_screen('title.txt'))
    players = []
    for i in range(2):
        players.append(Player(input("Enter player's name: ")))
        os.system('clear')
    n = 0
    while True:
        print('\n{} is shooting:\n'.format(players[n % 2].name))
        print_game_info(players[abs((n % 2) - 1)])
        shoot = players[n % 2].shoot()
        result = players[abs((n % 2) - 1)].handle_rivals_shoot(shoot)
        os.system('clear')
        print('\n{}'.format(result))
        check_winner(players)
        time.sleep(1)
        if result == 'You missed':
            n += 1


if __name__ == '__main__':
    main()

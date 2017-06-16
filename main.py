import sys
import time
import os
from player import *
from AI import *
import constants


def end_game(winner, loser):
    '''
    Function to print game sumary, and end program.

    Parameters:
    -----------
    winner - Player obj
    loser - Player obj
    '''
    try:
        print('\n'.join(read_file('game_over.txt')))
    except FileNotFoundError:
        print('GAME OVER')
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
    try:
        title_list = read_file(title_file)
        title = '\n'.join(title_list)
        width = len(title_list[1])
        allign = '^'
    except FileNotFoundError:
        title = 'BATTLESHIP\n'
        width = 25
        allign = '<'
    for author in constants.CREDITS:
        title += '\n{:{allign}{width}}'.format(author, allign=allign, width=width)

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


def make_players():
    '''
    Function to make players depending on users choice if he wants to face AI or other humanoid

    Return:
    -------
    list of Player obj
    '''
    players = []
    if ask_if_single_player():
        os.system('clear')
        players = [AI(), Player(input("Enter player's name: "))]
    else:
        for i in range(2):
            os.system('clear')
            players.append(Player(input("Enter player's name: ")))
    os.system('clear')
    return players


def main():
    print(make_title_screen('title.txt'))
    players = make_players()
    n = 0
    while True:
        print('\n{} is shooting:\n'.format(players[n % 2].name))
        players[abs((n % 2) - 1)].print_game_info()
        shoot = players[n % 2].shoot()
        result = players[abs((n % 2) - 1)].handle_rivals_shoot(shoot)
        players[n % 2].handle_shot_result(result)
        check_winner(players)
        time.sleep(2)
        os.system('clear')
        if result == 'Missed':
            n += 1


if __name__ == '__main__':
    main()

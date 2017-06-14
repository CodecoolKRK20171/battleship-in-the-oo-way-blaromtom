import sys, os
# from ocean import *
from player import Player
import constants


def end_game(winner, loser):
    print('\nGame Over\n')
    print('{} wins!'.format(winner.name))
    for player in [winner, loser]:
        print('\n{}\n'.format(player.name))
        player.ocean.print_board()
    sys.exit()


def check_winner(players):
    for i in range(len(players)):
        if all([ship.is_submerged for ship in players[i].ships]):
            loser = players[i]
            players.remove(loser)
            winner = players[0]
            end_game(winner, loser)


def main():
    players = []
    for i in range(2):
        players.append(Player(input("Enter player's name: ")))
        os.system('clear')
    n = 0
    while True:
        print('\n{} is shooting:\n'.format(players[n % 2].name))
        players[abs((n % 2) - 1)].ocean.print_board(show_hide=False)
        shoot = players[n % 2].shoot()
        result = players[abs((n % 2) - 1)].handle_rivals_shoot(shoot)
        os.system('clear')
        print('\n{}'.format(result))
        check_winner(players)
        if result == 'You missed':
            n += 1


if __name__ == '__main__':
    main()

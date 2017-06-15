# Battleship in the OOP way

## The story

Battleship (also Battleships or Sea Battle) is a guessing game for two players. It is played on ruled grids
(paper or board) on which the players' fleets of ships are marked. Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

## Specification


### `__main.py__`

This is the main file launching a game

__Functions__

* #### `end_game(winner, loser)`

 Function to print game summary and end program

* #### `read_file(file_name)`

 Function to read .txt file

* #### `make_title_screen(title_file)`

 Function to make title screen from title_file and credits
 Returns title as a string

* #### `check_winner(players)`

 Function to check if one of player is a winner, by checking if other one has lost all of his ships. If yes, runs end_game() function

* #### `print_game_info(player)`

 Function to print info about actual state of player and it's objects

### `__square.py__`

This file contain `square` Class and its logic

### Class Square

__Attributes__

### `__ship.py__`

### `__ocean.py__`

### `__constants.py__`

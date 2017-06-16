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

 Function to make title screen from *title_file* and credits
 Returns title as a string

* #### `check_winner(players)`

 Function to check if one of *player* is a winner, by checking if other one has lost all of his ships. If yes, runs end_game() function

### `__player.py__`

 Class for Player objects.

### Class Player

 __Attributes__

 * `name`
    - data: str
    - decription: player's name
 * `ocean`
    - data: Ocean obj
    - description: stores all squares

 __Instance methods__

* #### `__init__(self, name)`

 Constructs a `Player` object

 * `shoot(self)`

 Method to choose coordinate player want to shoot

* `handle_rivals_shoot(self, shoot)`

 Method to response for rivals *shoot* into given position(shoot)

* `handle_shot_result(self, result)`

 Prints *result*

* `print_game_info(self)`

 Function to print info about actual state of player and it's objects


### `__square.py__`

class of `square` obj - parts of `Ocean` and `Ship` objects


### Class Square

__Attributes__

* `ocean`
  - data: Ocean object
  - description: stores all squares

* `position`
  - data: tuple (int, int)
  - description: represents coordinates in square board

* `char`
  - data: string
  - description: represents the status of square depending on if it was shot and if it is empty(is not part of a `ship`)

* `was_shot`
  - data: boolean
  - description: describe whether the field (`square`) has beed shot

__Instance methods__

* #### `__init__(self, position, ocean)`

 Constructs a `square` object

* `__str__(self)`

 Returns char representing status of `square`

* `mark_as_missed(self)`

 Method to mark obj on board as missed by changing char attribute

* `mark_as_mast(self)`

 Method to mark obj on board as mast of ship by changing char attribute

* `mark_as_hit(self)`

 Method to mark obj on board as hit by changing char attribute

* `mark_as_submerged(self)`

 Method to mark obj on board as subemrged by changing char attribute

* `unmark(self)`

 Method to unmark obj on board as missed by changing char attribute

* `get_neighbour_squares(self, distance=1)`

 Method to get neighbour squares of self in given *distance*

**_@staticmethod_**
* `is_on_board(position)`

 Method to check if given *position* is in prewritten range of board height and width


### `__ship.py__`

### Class Ship

__Attributes__

* `ocean`
  - data: Ocean object
  - description: stores all squares

* `squares`
  - data: list of `Square` objects
  - description: represents in which squares the ship is

* `is_submerged`
  - data: boolean
  - description:  whether the whole ship is submerged

* `ship_type`
  - data: string
  - description: describes the type of ship

__Instance methods__

* #### `__init__(self, ocean, squares, ship_type)`

 Constructs a `Ship` object with default attribute *is_submerged* set as False

* `receive_hit(self, position)`

 Method to react on hit in given *position*

* `become_submerged(self)`

 Method to change slef attribute is_submerged and mark it on ocean

**_@staticmethods_**
* `form_straight_ship(ocean, ship_type, laying)`

 Used to get Squares objects of straight ship of given *ship_type* from given *ocean*

* `formed_curved_ship(ocean, ship_type)`

 Used to get Squares objects of curved ship of given type from given ocean


### `__ocean.py__`

### Class Ocean

__Attributes__

* `board`
  - data: list of lists of **Square** objects
  - description: represents a board to play on

* `ships`
  - data: list of **Ship** objects
  - description: all ships that appear on the *board*

__Instance methods__

* #### `__init__(self)`

 Creates board of height and width prewritten in constans module, and fills it with Square obj
 Runs place_ship() method

* `print_board(self, show_hide=False)`

 Method to print objects board with headers (taken from constants module). If *show_hide* is set to True, method prints whitespaces istead of **Square** obj which haven't been shot before

* `clear_board(self)`

 Method to unmark all Square objects from object's board

* `place_ships(self)`

 Method to place ships from list imported from constants module

* `make_ship(self, ship)`

 Method to create **_Ship_** object of given type, and add it to list

* `remove_ship(self, ship)`

 Method to remove **_Ship_** obj from list


 ### `__constants.py__`

  Contains module with constant values needed in other modules


 ### `__UI.py__`

  Contains function of user interface

 __Module functions__

 * `set_ship_layint()`

  Function to set laying of ship depends on user input

 * `get_confirmation(question)`

  Function to get confirmation from user

 * `get_coordinate(input_text)`

  Function to get correct coordinate from user. It uses data from constants module

 * `choose_ship(available_ships)`

  Function to let user choose ship form given *available_ships* list



### `__AI.py__`

### Class AI

Class that inherits from **Player** class
Class for Artifician Inteligence player

__Attributes__

* `name`
  - data: str
  - description: represents a name of player

* `ocean`
  - data: **Ocean** object
  - description: dd

* `rivals_ocean`
  - data: **Ocean** object
  - description: represents the rival's ocean

* `expected_ship`
  - data: list od **Square** objects
  - description: store info about where to expect next ship

* `previous_shots`
  - data: list of **Square** objects
  - description: store info about where previous shots have beed

__Instance methods__

* #### `__init__(self)`

 Construct an AI object as a computer player

* `shoot(self)`

 Method to choose random or consequent position of shoot

* `handle_shot_result(self, result)`

 Method to handle and react to *result* of self previous shot

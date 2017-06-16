import constants


def ask_if_single_player():
    '''
    Function to ask user if he wants to play in sigle player mode

    Return:
    -------
    bool
    '''
    print('(1) - One player\n(2) - Two players')
    while True:
        choose = input('Choose option: ')
        if choose == '1':
            return True
        elif choose == '2':
            return False


def set_ship_laying():
    '''
    Function to set laying of ship depends on user input

    Return:
    -------
    str
    '''
    while True:
        input_text = "\nEnter 'V', 'H', 'C' to place ship vertically, horizontally or curved, 'R' to place ship in random place: "
        choose = input(input_text)
        if choose.lower() == 'v':
            return 'vertical'
        elif choose.lower() == 'h':
            return 'horizontal'
        elif choose.lower() == 'c':
            return 'curved'
        elif choose.lower() == 'r':
            return 'random'

        else:
            print('Wrong choose')


def get_confirmation(question):
    '''
    Function to get confirmation from user

    Arguments:
    ----------
    question - str

    Return:
    -------
    bool
    '''
    if input(question).lower() == 'y':
        return True
    else:
        return False


def get_coordinate(input_text):
    '''
    Function to get correct coordinate from user.
    It uses data from constants module

    Arguments:
    ----------
    input_text - str

    Return:
    -------
    tuple (int, int)
    '''
    while True:
        choose = input(input_text).upper()
        try:
            if len(choose) < 2:
                raise ValueError
            elif choose[0] not in constants.COLLUMNS_NAME_INDEX or int(choose[1:]) not in constants.COLLUMNS_NAME_INDEX.values():
                raise ValueError
        except (TypeError, ValueError):
            print('Wrong coordinate!')
        else:
            return constants.COLLUMNS_NAME_INDEX[choose[0]] - 1, int(choose[1:]) - 1


def choose_ship(available_ships):
    '''
    Function to let user choose ship form given available_ships list

    Arguments:
    ----------
    available_ships - list of str

    Return:
    -------
    str
    '''
    print('\nAvailable ships:\n')
    for i in range(len(available_ships)):
        print('{0} - {1} (lenght: {2} squares)'.format(i + 1, available_ships[i],
                                                       constants.SHIPS_TO_PLACE[available_ships[i]]))
    print('\n{} - remove last placed ship'.format(len(available_ships) + 1))
    while True:
        try:
            choose = int(input('\nEnter number to choose: '))
            if choose - 1 in range(len(available_ships)):
                return available_ships[choose - 1]
            elif choose - 1 == len(available_ships):
                return
            else:
                raise ValueError
        except ValueError:

            print('Wrong choose!')

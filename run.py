"#storyboard"
# x for taking the ship and hit battleship
# ' ' for available space
# '-' for missed shot

from random import randint

# Introduction to the game

introduction = 'Welcome to Battleship-8040'
print(introduction)

# Instructions to the game and how to play

enter = input('Type Enter to start the game:')
while not enter:
    print('Invalid input. Try again')
    enter = input('Type Enter to start the game:')


print('The battleship is 9 cells long')
print('The battleship is hidden in a 9x9 board')
print('The board is labeled with numbers 1-9 and letters A-I')
print('You will enter the row and column to hit the battleship')
print('If you hit the battleship, you will see an X')
print('If you miss the battleship, you will see a -')
print('You can only hit each cell once')
print('You win by hitting the battleship 6 times')
print('Good luck')

name = input('Enter your name:')
while not name:
    print('Invalid input. Try again')
    name = input('Enter your name:')
print('Hello ' + name)


"""
game boards
BOARD_GAME_HIDDEN is the board with the battleship hidden
GAME_GUESS_BOARD is the board where the player will guess the location
of the battleship

"""
BOARD_GAME_HIDDEN = [[' '] * 9 for _ in range(9)]
GAME_GUESS_BOARD = [[' '] * 9 for _ in range(9)]
letter_for_number = {'A': 0,
                     'B': 1,
                     'C': 2,
                     'D': 3,
                     'E': 4,
                     'F': 5,
                     'G': 6,
                     'H': 7,
                     'I': 8
                     }


"""
Function print board
This function will print the board with the battleship hidden
and the board where the player will guess the location of the battleship
:param board: list of lists
:return: None

"""

print('board of:' + name)


def print_board(board):
    print('  A B C D E F G H I')
    print(' -------------------')
    row_number = 1
    """for loop"""
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    print(' -------------------')


"""Function ship create
This function will create the battleship on the board
:param board: list of lists
:return: None"""


def ship_create(board):
    for _ in range(6):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 8), randint(0, 8)
        board[ship_row][ship_column] = 'X'


"""Function get ship row number column letter
This function will get the row number and column letter from the player
:param: None
:return: tuple of integers row number and column letter as integers
"""


def get_ship_row_number_column_letter():
    while True:
        try:
            row = input('Enter the row number: 1-9 :')
            while not row or int(row) < 1 or int(row) > 9:
                print('Invalid input. Try again')
                row = input('Enter the row number: 1-9 :')
            row = int(row)

            column = input('Enter the column letter: A-I :')
            while not column or column.upper() not in letter_for_number:
                print('Invalid input. Try again')
                column = input('Enter the column letter: A-I :')

            column = letter_for_number[column.upper()]
            if row < 1 or row > 9 or column < 0 or column > 8:
                print('Invalid input. Try again')
                continue
            elif GAME_GUESS_BOARD[row - 1][column] != ' ':
                print('You already guessed that location. Try again')
                continue
            else:
                return row - 1, column
        except ValueError:
            print("Invalid input."),
            ("Please enter a valid.row,number and column letter.")
            continue
        except KeyError:
            print("Invalid input."),
            ("Please enter a valid row number and column letter.")
            continue


"""Function count hit
This function will count the number of hits on the battleship
:param board: list of lists
:return: integer count of hits on the battleship"""


def count_hit(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


"""
ship create
This will create the battleship on the board
:param BOARD_GAME_HIDDEN: list of lists
:return: None

"""

ship_create(BOARD_GAME_HIDDEN)
turns = 10
game_over = False
score = 0
while not game_over and turns > 0:
    print('Welcome to Battleship-8040')
    print_board(GAME_GUESS_BOARD)
    print('You have ' + str(turns) + ' turns remaining')
    print('you have ' + str(score) + ' hits')
    row, column = get_ship_row_number_column_letter()
    if GAME_GUESS_BOARD[row][column] == '-':
        print('You already guessed it')
        print('Try Again', + name)
        continue
    elif BOARD_GAME_HIDDEN[row][column] == 'X':
        print('Congratulations')
        print('You hit the battleship')
        score += 1
        GAME_GUESS_BOARD[row][column] = 'X'
    else:
        print('You Missed')
        GAME_GUESS_BOARD[row][column] = '-'
        print('Try Again:' + name)
    turns -= 1
    if count_hit(GAME_GUESS_BOARD) == 6:
        print('Congrats You Win !!!')
        print('You hit the battleship 6 times')
        print('You have ' + str(turns) + ' turns remaining')
        print('your score is ' + str(score) + ' hits')
        game_over = True
    elif turns == 0:
        print('Game Over. You ran out of turns.')
        game_over = True
    if not game_over:
        print('You have ' + str(turns) + ' Remaining turns')
        print('You have ' + str(score) + ' hits')
        print('Try Again:' + name)
    else:
        print('Game Over')
        print('The ship was hidden at:')
        print_board(BOARD_GAME_HIDDEN)
        print('Your guesses were:')
        print_board(GAME_GUESS_BOARD)
        print('Thanks for playing')
        break

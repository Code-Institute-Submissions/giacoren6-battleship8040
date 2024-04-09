# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#storyboard
# x for taking the ship and hit battleship
# ' ' for avalible space
# '-' for missed shot


introduction = 'Welcome to Battleship-8040'
print(introduction)

input('Press Enter to start the game:')
print('The battleship is 8 cells long')
print('The battleship is hidden in a 9x9 board')
print('The board is labeled with numbers 1-9 and letters A-I')
print('You will enter the row and column to hit the battleship')
print('If you hit the battleship, you will see an X')
print('If you miss the battleship, you will see a -')
print('You can only hit each cell once')
print('You win by hitting the battleship 6 times')
print('Good luck')

name = input('Enter your name:')
print('Hello ' + name)

from random import randint
"""game boards"""
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


"""Function print board"""

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


"""Function ship create """


def ship_create(board):
    for _ in range(6):
        ship_row, ship_column = randint(0, 8), randint(0, 9)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 8), randint(0, 9)
        board[ship_row][ship_column] = 'X'


"""Function location ship"""
def get_ship_location():
    while True : 
        try: 
            row = int(input('Enter the row number: 1-9 :'))
            column = input('Enter the column letter: A-I :')
            column = letter_for_number[column.upper()]
            if row < 1 or row > 9 or column < 0 or column > 8:
                print('Invalid input. Try again')
                continue
            else:
                return row - 1, column
        except ValueError:
            print("Invalid input. Please enter a valid row number and column letter.")
            continue
        except KeyError:
            print("Invalid input. Please enter a valid row number and column letter.")


def count_hit(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

"""Function winner and loser"""
 
# Assuming the necessary functions and variables are defined elsewhere
# ship_create(BOARD_GAME_HIDDEN)
# BOARD_GAME_HIDDEN, GAME_GUESS_BOARD = ..., ...
# def get_ship_location(): ...
# def count_hit(board): ...
 
turns = 10
game_over = False
 
while not game_over:
    print('Welcome to Battleship-8040')
    print_board(GAME_GUESS_BOARD)
    row, column = get_ship_location()
    if GAME_GUESS_BOARD[row][column] == '-':
        print('You already guessed it')
    elif BOARD_GAME_HIDDEN[row][column] == 'X':
        print('Congratulations')
        GAME_GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('You Missed')
        GAME_GUESS_BOARD[row][column] = '-'
        turns -= 1
 
    if count_hit(GAME_GUESS_BOARD) == 6:
        print('Congrats You Win !!!')
        game_over = True
    elif turns == 0:
        print('Game Over')
        game_over = True
 
    if not game_over:
        print('You have ' + str(turns) + ' Remaining turns')
        print('the ship hidden in the board')
        print(BOARD_GAME_HIDDEN)
        print('Try Again')

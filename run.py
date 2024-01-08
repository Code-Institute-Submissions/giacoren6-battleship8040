# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#storyboard
# x for taking the ship and hit battleship
# ' ' for avalible space
# '-' for missed shot

from random import randint
"""game boards"""
BOARD_GAME_HIDDEN = [[' '] * 9 for x in range(9)]
GAME_GUESS_BOARD = [[' '] * 9 for x in range(9)]
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
"""class print board"""


def print_board(board):
    print('  A B C D E F G H I')
    print(' -------------------')
    row_number = 1
    """for loop"""
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


"""class ship create """


def ship_create(board):
    for ship in range(6):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 8), randint(0, 8)
        board[ship_row][ship_column] = 'X'


"""class location ship"""


def get_ship_location():
    row = input('Enter a ship row 1-9:')
    while row not in '1 2 3 4 5 6 7 8 9':
        print('Enter a valid row')
        row = input('Enter a ship row 1-9')
    column = input('Enter a ship column  A-I:').upper()
    while column not in 'ABCDEFGHI':
        column = input('Enter a ship column  A-I:').upper()
    return int(row) - 1, letter_for_number[column]


"""class hit board count"""


def count_hit(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


"""class winner and loser"""


def game_over_and_win():
    pass

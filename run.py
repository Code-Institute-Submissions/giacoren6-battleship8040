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


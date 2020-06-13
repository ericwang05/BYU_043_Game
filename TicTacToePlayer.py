# import random
# class Player:
#     def inputPlayerLetter(self):
#         # Lets the player type which letter they want to be.
#         # Returns a list with the player's letter as the first item, and the computer's letter as the second.
#         letter = ''
#         while not (letter == 'X' or letter == 'O'):
#             print('Do you want to be X or O?')
#             letter = input().upper()

#         # the first element in the tuple is the player's letter, the second is the computer's letter.
#         if letter == 'X':
#             return ['X', 'O']
#         else:
#             return ['O', 'X']

#     def makeMove(self):
#         board[move] = letter

import random
class Player:
    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def makeMove(self):
        board[move] = letter


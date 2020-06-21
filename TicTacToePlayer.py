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
    def __init__(self):
        self.playerLetter=''
    def inputPlayerLetter(self,turn):

        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print(turn + " , what is your letter?:")
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if turn == "Player 1" or turn=='Player':
            if letter=='X':
                return ('X', 'O')
            else:
                return ('O', 'X')
        else:
            if letter=='X':
                return ('O', 'X')
            else:
                return ('X', 'O')


    def makeMove(self,board,move):
        board[move] = self.playerLetter

    def isWinner(self, bo):
        le=self.playerLetter
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


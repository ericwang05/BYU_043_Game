# import random
# from TicTacToePlayer import Player

# print(Player)
# class Computer(Player):
#     def chooseRandomMoveFromList(self):
#         # Returns a valid move from the passed list on the passed board.
#         # Returns None if there is no valid move.
#         possibleMoves = []
#         for i in movesList:
#             if isSpaceFree(board, i):
#                 possibleMoves.append(i)

#         if len(possibleMoves) != 0:
#             return random.choice(possibleMoves)
#         else:
#             return None
#     def getComputerMove(self, board, computerLetter):
#         # Given a board and the computer's letter, determine where to move and return that move.
#         if computerLetter == 'X':
#             playerLetter = 'O'
#         else:
#             playerLetter = 'X'

#         # Here is our algorithm for our Tic Tac Toe AI:
#         # First, check if we can win in the next move
#         for i in range(1, 10):
#             copy = getBoardCopy(board)
#             if isSpaceFree(copy, i):
#                 makeMove(copy, computerLetter, i)
#                 if isWinner(copy, computerLetter):
#                     return i

#         # Check if the player could win on his next move, and block them.
#         for i in range(1, 10):
#             copy = getBoardCopy(board)
#             if isSpaceFree(copy, i):
#                 makeMove(copy, playerLetter, i)
#                 if isWinner(copy, playerLetter):
#                     return i

#         # Try to take one of the corners, if they are free.
#         move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
#         if move != None:
#             return move

#         # Try to take the center, if it is free.
#         if isSpaceFree(board, 5):
#             return 5

#         # Move on one of the sides.
#         return chooseRandomMoveFromList(board, [2, 4, 6, 8])

import random
from TicTacToePlayer import Player
from TicTacToeBoard import Board

print(Player)
class Computer(Player):
    def chooseRandomMoveFromList(self):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def isSpaceFree(self, board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def makeMove(self, board, letter, move):
        board[move] = letter

    def isWinner(self, bo, le):
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

    def chooseRandomMoveFromList(self, board, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(self, board, computerLetter):
        # Given a board and the computer's letter, determine where to move and return that move.
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        b = Board()
        for i in range(1, 10):
            copy = b.getBoardCopy(board)
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, computerLetter, i)
                if self.isWinner(copy, computerLetter):
                    return i

        # Check if the player could win on his next move, and block them.
        for i in range(1, 10):
            copy = b.getBoardCopy(board)
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, playerLetter, i)
                if self.isWinner(copy, playerLetter):
                    return i

        # Try to take one of the corners, if they are free.
        move = self.chooseRandomMoveFromList(board, [1, 3, 7, 9])
        if move != None:
            return move

        # Try to take the center, if it is free.
        if self.isSpaceFree(board, 5):
            return 5

        # Move on one of the sides.
        return self.chooseRandomMoveFromList(board, [2, 4, 6, 8])

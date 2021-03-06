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


class Computer(Player):

    def chooseRandomMoveFromList(self, board, movesList):
        b=Board()
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if b.isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(self, board, player):
        # Given a board and the computer's letter, determine where to move and return that move.


        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        b = Board()
        for i in range(1, 10):
            copy = b.getBoardCopy(board)
            if b.isSpaceFree(copy, i):
                self.makeMove(copy, i)
                if self.isWinner(copy):
                    return i

        # Check if the player could win on his next move, and block them.
        for i in range(1, 10):
            copy = b.getBoardCopy(board)
            if b.isSpaceFree(copy, i):
                player.makeMove(copy, i)
                if player.isWinner(copy):
                    return i

        # Try to take one of the corners, if they are free.
        move = self.chooseRandomMoveFromList(board, [1, 3, 7, 9])
        if move != None:
            return move

        # Try to take the center, if it is free.
        if b.isSpaceFree(5,move):
            return 5

        # Move on one of the sides.
        return self.chooseRandomMoveFromList(board, [2, 4, 6, 8])

    def inputPlayerLetter(self):

        if random.randint(0,2)==1:
            return ('X', 'O')
        else:
            return ('O', 'X')




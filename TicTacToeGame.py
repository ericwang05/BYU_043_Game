import random
from TicTacToeComputerPlayer import Computer
from TicTacToePlayer import Player


class TicTacToeGame:
    def __init__(self):
        self.numOfPlayers = 0
        self.player1=None
        self.player2=None

    def howManyPlayers(self):
        while self.numOfPlayers not in [1,2]:
            print("How many players are there?(1 or 2):", end="")
            self.numOfPlayers = int(input())

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            if self.numOfPlayers == 1:
                return 'computer'
            else:
                return 'player 2'
        else:
            if self.numOfPlayers == 1:
                return 'player'
            else:
                return 'player 1'
    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')
    def isWinner(self,bo,le):
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
    def getPlayerMove(self):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)
    def play(self):
        print(
            'Welcome to Tic Tac Toe!\nJust so you know, 1 is the lower left hand corner, and 9 is the upper right corner.')
        self.howManyPlayers()
        if self.numOfPlayers == 1:
            self.player1 = Player()
            self.player2 = Computer()
        else:
            self.player1 = Player()
            self.player2 = Player()
        if self.numOfPlayers == 1:
            while True:
                # Reset the board
                theBoard = [' '] * 10
                playerLetter, computerLetter = Player().inputPlayerLetter()
                turn = TicTacToeGame().whoGoesFirst()
                print('The ' + turn + ' will go first.')
                gameIsPlaying = True

                while gameIsPlaying:
                    if turn == 'player':
                        # Player's turn.
                        drawBoard(theBoard)
                        move = getPlayerMove(theBoard)
                        makeMove(theBoard, playerLetter, move)

                        if isWinner(theBoard, playerLetter):
                            drawBoard(theBoard)
                            print('Hooray! You have won the game!')
                            gameIsPlaying = False
                        else:
                            if isBoardFull(theBoard):
                                drawBoard(theBoard)
                                print('The game is a tie!')
                                break
                            else:
                                turn = 'computer'

                    else:
                        # Computer's turn.
                        comp=Computer()
                        comp.board=theBoard
                        comp.computerLetter=computerLetter
                        move = comp.getComputerMove(theBoard, computerLetter)
                        makeMove(theBoard, computerLetter, move)

                        if isWinner(theBoard, computerLetter):
                            drawBoard(theBoard)
                            print('The computer has beaten you! You lose.')
                            gameIsPlaying = False
                        else:
                            if isBoardFull(theBoard):
                                drawBoard(theBoard)
                                print('The game is a tie!')
                                break
                            else:
                                turn = 'player'

                if not playAgain():
                    break
        else:
            while True:
                # Reset the board
                theBoard = [' '] * 10
                playerLetter, computerLetter = inputPlayerLetter()
                turn = whoGoesFirst()
                print(turn + ' will go first.')
                gameIsPlaying = True

                while gameIsPlaying:
                    if turn == 'player 1':
                        # Player's turn.
                        drawBoard(theBoard)
                        move = getPlayerMove(theBoard)
                        makeMove(theBoard, playerLetter, move)

                        if isWinner(theBoard, playerLetter):
                            drawBoard(theBoard)
                            print('Hooray!', playerLetter, 'has won the game!')
                            gameIsPlaying = False
                        else:
                            if isBoardFull(theBoard):
                                drawBoard(theBoard)
                                print('The game is a tie!')
                                break
                            else:
                                turn = 'player2'

                    else:
                        # Player's turn.
                        drawBoard(theBoard)
                        move = getPlayerMove(theBoard)
                        makeMove(theBoard, computerLetter, move)

                        if isWinner(theBoard, computerLetter):
                            drawBoard(theBoard)
                            print('Hooray!', computerLetter, ' has won the game!')
                            gameIsPlaying = False
                        else:
                            if isBoardFull(theBoard):
                                drawBoard(theBoard)
                                print('The game is a tie!')
                                break
                            else:
                                turn = 'player 1'

                if not playAgain():
                    break





game=TicTacToeGame() #How many players?
game.play()


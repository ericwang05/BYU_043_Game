import random
from TicTacToeComputerPlayer import Computer
from TicTacToePlayer import Player
from TicTacToeBoard import Board


class TicTacToeGame:
    def __init__(self):
        self.numOfPlayers = 0
        self.player1=None
        self.player2=None

    def howManyPlayers(self):
        self.numOfPlayers=0
        while self.numOfPlayers not in [1,2]:
            print("How many players are there?(1 or 2):", end="")
            self.numOfPlayers = int(input())


    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
            if self.numOfPlayers == 1:
                if random.randint(2,3) == 2:
                    return 'Computer'
                else:
                    return 'Player'
            if self.numOfPlayers == 2:
                if random.randint(1, 2) == 1:
                    return 'Player 1'
                else:
                    return 'Player 2'
    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')



    def getPlayerMove(self, b, board,turn):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not b.isSpaceFree(board, int(move)):
            print(turn +', what is your next move? (1-9)')
            move = input()
        return int(move)
    def play(self):
        print(
            'Welcome to Tic Tac Toe!\n')

        score=[0,0]
        while True:
            lastgamenum=self.numOfPlayers
            self.howManyPlayers()
            if self.numOfPlayers!=lastgamenum:
                score = [0, 0]
            if self.numOfPlayers == 1:
                self.player1 = Player()
                self.player2 = Computer()
            else:
                self.player1 = Player()
                self.player2 = Player()
            pnum = self.numOfPlayers
            if pnum == 1:
                # Reset the board
                theBoard = [' '] * 10
                b = Board()

                turn = self.whoGoesFirst()
                print('\n' + str(turn).upper() + ' will go first.\n')
                if turn=='Player':
                    (playerLetter, computerLetter) = Player().inputPlayerLetter(turn)
                    self.player1.playerLetter = playerLetter
                    self.player2.playerLetter = computerLetter
                else:
                    (playerLetter, computerLetter) = Computer().inputPlayerLetter()
                    self.player1.playerLetter = playerLetter
                    self.player2.playerLetter = computerLetter
                    print(playerLetter + " is your letter, Player\n")

                print('Just so you know, 1 is the lower left hand corner, and 9 is the upper right corner.\n')

                gameIsPlaying = True

                while gameIsPlaying:
                    if turn == 'Player':
                        # Player's turn.
                        b.drawBoard(theBoard)
                        move = self.getPlayerMove(b, theBoard,turn)
                        self.player1.makeMove(theBoard, move)

                        if self.player1.isWinner(theBoard):
                            b.drawBoard(theBoard)
                            print('Hooray! You have won the game!')
                            score[0]+=1
                            gameIsPlaying = False
                        else:
                            if b.isBoardFull(theBoard):
                                b.drawBoard(theBoard)
                                print('The game is a tie!')
                                break
                            else:
                                turn = 'Computer'

                    else:
                        if turn=="Computer":
                            # Computer's turn.
                            move = self.player2.getComputerMove(theBoard, self.player1)
                            self.player2.makeMove(theBoard,move)

                            if self.player2.isWinner(theBoard):
                                b.drawBoard(theBoard)
                                print('The Computer has beaten you! You lose.')
                                score[1]+=1
                                gameIsPlaying = False
                            else:
                                if b.isBoardFull(theBoard):
                                    b.drawBoard(theBoard)
                                    print('The game is a tie!')
                                    break
                                else:
                                    turn = 'Player'
                print("Stats\nPlayer: {}\nComputer: {}".format(score[0], score[1]))
                if not self.playAgain():
                    return
            else:
                # Reset the board
                theBoard = [' '] * 10
                b = Board()
                p = Player()

                turn = self.whoGoesFirst()
                print('\n' + str(turn).upper() + ' will go first.\n')
                (player1Letter, player2Letter) = p.inputPlayerLetter(turn)
                self.player1.playerLetter = player1Letter
                self.player2.playerLetter = player2Letter
                print('Just so you know, 1 is the lower left hand corner, and 9 is the upper right corner.\n')

                gameIsPlaying = True

                while gameIsPlaying:
                    if turn == 'Player 1':
                        # Player's turn.
                        b.drawBoard(theBoard)
                        move = self.getPlayerMove(b, theBoard,turn)
                        self.player1.makeMove(theBoard, move)

                        if self.player1.isWinner(theBoard):
                            b.drawBoard(theBoard)
                            print('Hooray! '+ 'Player 1'+ ' has won the game!')
                            score[0]+=1
                            gameIsPlaying = False
                        else:
                            if b.isBoardFull(theBoard):
                                b.drawBoard(theBoard)
                                print('The game is a tie!')
                                break
                            else:
                                turn = 'Player 2'

                    else:
                        if turn=="Player 2":
                            b.drawBoard(theBoard)
                            move = self.getPlayerMove(b, theBoard,turn)
                            self.player2.makeMove(theBoard,move)

                            if self.player2.isWinner(theBoard):
                                b.drawBoard(theBoard)
                                print('Hooray! '+ 'Player 2' + ' has won the game!')
                                score[1]+=1
                                gameIsPlaying = False
                            else:
                                if b.isBoardFull(theBoard):
                                    b.drawBoard(theBoard)
                                    print('The game is a tie!')
                                    break
                                else:
                                    turn = 'Player 1'
                print("Stats\nPlayer 1: {}\nPlayer 2: {}".format(score[0], score[1]))
                if not self.playAgain():
                    return


game=TicTacToeGame()
game.play()

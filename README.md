# Introduction

Hi. We are Benjamin Chen, Eric Wang, and Gursirat Singh, authors of this Tic Tac Toe game. There can be 1 player or 2 players, depending on what the user wants. Libraries used: random.

## Features
Additional features:
- There is now a scorekeeping function!!! One for the main player, the other for the computer/secondary player
- After finishing the game, the user will be prompted again for the amount of players. This is useful if you don't want your score to reset.

## Gameplay

To run the game, there are a few options:
- Run the file in the command line:

```python3 TicTacToeGame.py```


*note that to run the file in the terminal without errors, you have to say "python3," not "python."
- Open the file using an interpreter like IDLE and run it

The user will:
- Need a keyboard

You will first:

Choose your mode: (1-player or 2-player)

The board will be loaded

Then Enter whether you would like to be X or O by typing the letter in when prompted.

The computer will randomly choose who gets to start if you choose the mode to be 2 player then it will choose a random player to start, if 1 player, either the computer or the player will get to start. 

For your move you will have a box such as this:
```
   |   |
   |   |  
   |   |
-----------
   |   |
   |   |  
   |   |
-----------
   |   |
   |   |  
   |   |
```
The numbers represent the number you will have to choose to select where your marker goes each turn.
This will be repeated until either the board is filled (tie) or a player wins.
If the space is not available you will be prompted again for your selection.
Goal:
To get three of your marker in a row first
Try to stop your opponent from doing the same.

Once the game is over the winner will be announced and you will be asked if you want to play again. The scoreboard will also be displayed.
If so, type in: “yes” → If you typed in yes, you will be reset and asked game mode(number of players)
If not type: anything other than yes



```
Welcome to Tic Tac Toe!

How many players?: 2

PLAYER 1 will go first.

Player 1 , what is your letter?:
x
Just so you know, 1 is the lower left hand corner, and 9 is the upper right corner.

   |   |
   |   |  
   |   |
-----------
   |   |
   |   |  
   |   |
-----------
   |   |
   |   |  
   |   |
Player 1, what is your next move? (1-9)
1
   |   |
   |   |  
   |   |
-----------
   |   |
   |   |  
   |   |
-----------
   |   |
 X |   |  
   |   |
Player 2, what is your next move? (1-9)
5
   |   |
   |   |  
   |   |
-----------
   |   |
   | O |  
   |   |
-----------
   |   |
 X |   |  
   |   |
Player 1, what is your next move? (1-9)
7
   |   |
 X |   |  
   |   |
-----------
   |   |
   | O |  
   |   |
-----------
   |   |
 X |   |  
   |   |
Player 2, what is your next move? (1-9)
4
   |   |
 X |   |  
   |   |
-----------
   |   |
 O | O |  
   |   |
-----------
   |   |
 X |   |  
   |   |
Player 1, what is your next move? (1-9)

```

## Computer Algorithm

The computer works by:
1. seeing if the computer can win in one move
2. seeing if the computer can block the player from winning
3. choosing a corner, if available
4. choosing the center, if available
5. choosing an edge, if available

Stopping if there are no more spaces left on the board ensures that there will never be an error when the computer decides its move.

Design:
For our game, we have several classes (Computer player, Player, TicTacToeGame, and Board)
Our TicTacToeGame is the main class that we are using because it is the game itself
Inside of the TicTacToeGame class, we create objects for the players, computers, and the board
We then call the methods from the other classes and the class functions from TicTacToeGame in order for the player to be able to see the board, interact with it, and play either with a computer or another player

Information about the Player class:
InputPlayerLetter(): For this function, we prompt our user to pick to be either an X or an O. If the player chooses X, the computer or second player will be an O and vice versa
We will be using the letters later to mark the spots each of the players previously chose
makeMove(): The player’s chosen spot becomes marked with their player letter’

Information about the ComputerPlayer class:
chooseRandomMoveFromList: The computer player will have a list of all of the valid moves that it can do and chooses a random move
isSpaceFree(): The computer player checks if the spot that it picked on the board is already occupied
makeMove(): The computer’s chosen spot becomes marked with its letter
isWinner(): The board gets checked if whether or not the computer player won by checking if the diagonals are all filled up with only the computer letter, a column is filled with only the computer letter, or if a row is filled with only the computer letter
getComputerMove(): (Algorithm for our computer player’s AI) The computer goes through several steps to make a move:
Makes a copy of the board with getBoardCopy() from the Board class
Checks, if it can win this turn with isWinner() and marks that spot is isSpaceFree()
Decides on a random move on a corner with chooseRandomMoveFromList()
While deciding on a random move on the corners, it checks whether the chosen space is free with isSpaceFree()
If the center is not taken yet, it will check if isSpaceFree() and then take the spot if it is
If it cannot take a corner, game-winning spot, or center, the computer player will call chooseRandomMoveFromList() with a list of the available spots that are on the sides of the boards 

Information about Board class:
drawBoard(): Prints out the current state of the board with all of the open spaces or spaces taken with a player letter
getBoardCopy(): Returns a copy of the board so it can be used for the players to make moves
isSpaceFree(): Checks whether the current spot has a player letter or not
isBoardFull(): Checks if all of the spots on the board are already taken, this function helps us determine if the game is a tie

Information about TicTacToeGame class: 
__init__(): We keep track of how many players we have and we keep track of a Player object for both player 1 and player 2
howManyPlayers(): The game prompts the user to input how many players are playing the game
makeMove(): The game board gets marked with a player letter
whoGoesFirst(): The game randomly chooses a number and depending on that number, player 1, player 2, or the AI will go first.
playAgain(): Prompts the user to decide whether they want to play again
isWinner(): Checks the board to see whether there is a game-winning pattern with only one type of player letter
getPlayerMove(): Asks the player to pick a position on the board to mark
play(): The main function we call to actually play the game




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

Here is an example of gameplay.

```
Welcome to Tic Tac Toe!

How many players are there?(1 or 2):2
Do you want to be X or O?
x
player 1 will go first.
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
What is your next move? (1-9)
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
What is your next move? (1-9)
```
The player can choose how many people play the game (1 or 2), and the first person to go can choose to be X or O.

To place a marker, the current player inputs an eligible number to substitute their marker with that number (if that number doesn't exist, then the player will be prompted again). Then, their turn ends and gameplay switches to the other player (or the computer in 1 player mode).

The game ends when:
- one player places 3 markers in a row
- there are no more available markers left on the board

## Computer Algorithm

The computer works by:
1. seeing if the computer can win in one move
2. seeing if the computer can block the player from winning
3. choosing a corner, if available
4. choosing the center, if available
5. choosing an edge, if available

Stopping if there are no more spaces left on the board ensures that there will never be an error when the computer decides its move.

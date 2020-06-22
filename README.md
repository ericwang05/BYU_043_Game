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

Need a keyboard
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


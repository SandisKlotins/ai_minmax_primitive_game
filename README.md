# ai_minmax_primitive_game

## Getting started
Tested on python 3.9, 3.10, and 3.11.
Dependencies: built in tkinter library.

run the start.py file

## Rules
Two player game.
Each player has 80 total points semi-randomly distributed in health and shield points.
The game is won by the player who gets opponent to 0 or below 0 health points.
To win the game player (and AI) has to evaluate which spell combination takes the least
amount of turns to lead to the victory condition.

## How to play
- User is prompted to choose their player (Player 1/Player 2). 
Ai automatically is assigned the leftover player.
- User is prompted to choose which of the two players makes the first turn (Player 1/Player 2).
- 4 progress bars appear, 2 for each player. One progress bar represents health, the other shields.
- Player has to figure out which combination of spells takes the least amount of turns to get opponents health to 0.
- Player and AI can cast a single spell on each turn (fire/frost). Each spell decrements opponents health and/or shields.
- fire deals 5 points of health and 5 points of shield damage if opponent 1 or more shield points remaining. If opponent does not have any more shields the spell does 10 points of health damage
- frost deals 15 points of shield and 0 points of health damage if opponent has 1 or more shield points remaining. If opponent does not have any more shields the pell does 5 points of health damage.
- Turns repeat until victory conditon is met
- The user can choose to play again.

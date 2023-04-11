# MinMax primitive game

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

# Technical implementation
## Game tree
Code for game tree realization can be found in TurnTree.py and visualization of turns can be found in turn_example.py.

Algorithm starts by generating a root node
Root node (and all the following nodes) are stored as dicts of list of dicts. 
- First dict key represents the turn (0 for root node, 1 for first turn etc). 
- Key value is a single list that stores all possible outcomes for that turn (1 possible outcome for root node, 2 outcomes for turns one, 4 outcomes for turn two etc).
- Each element of the list is a dict containing metadata of possible turn's outcome.
    - **id** = unique id of possible outcome
    - **previous_id** = set of unique ids from previous outcomes that lead to this outcome
    - **p1** = dict storing player 1's health and shield values
    - **p2** = dict storing player 2's health and shield values
    - **player** = identifies which player is making the turn (Player 1/Player 2)
    - **spell** = identifies which spell leads to outcome
    - **rating** = rating if outcome is good for AI (1 =  good outcome, -1 = bad outcome, None = tree not evaluated yet)

![Alt text](./media/ex1.PNG?raw=true "Outcome example")
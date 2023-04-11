# MinMax primitive game

## Getting started
Tested on python 3.9, 3.10, and 3.11.  
Dependencies: built in tkinter library.  
Run the start.py file.  

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
- Fire deals 5 points of health and 5 points of shield damage if opponent has 1 or more shield points remaining. If opponent does not have any shields the spell does 10 points of health damage
- Frost deals 15 points of shield and 0 points of health damage if opponent has 1 or more shield points remaining. If opponent does not have shields the spell does 5 points of health damage.
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
New turns and nodes are iteratively generated until player 1 and player 2 have 0 or less health in every outcome.  
Game tree generation completes.  

## Optimizations
With point pool capped at 80 all outcomes get processed on average in 26 turns. With no optimization this can be a rough amount to process 
e.g. turn 25 would have 2^25 = 33554432 outcomes, however, a deduplication procedure is used.  
Deduplication is achieved by storing each outcome's stats in a tuple and appending it to a list of seen outcomes. If any of the following outcomes has the same values then it is not appended as a new option, instead that outcome's id gets added to exisitng outcome's previous_id set. This can be though of as a converging multiple outcomes into one outcome.
As a result we get couple of hundered options instead of millions.
![Alt text](./media/ex5.PNG?raw=true "Dedup example")

## Game tree evaluation
Game tree is evaluated from bottom to top.  
Evaluation starts by taking the last turn (last list) from the game tree turns dict.  
Eavluation process is simple:  
If human player has 0 or less health then rating = 1 else rating = -1 (there can be no neutral rating, one player has to die).  
After evaluaing the root node the script evaluates the next node.  
If next node contains id is seen in previous turn's nodes previous_id set then the current node inherits previous node's rating.  
If id cannot be found in previous turn's previous_id set then the node is considered dead end node and a new rating is assigned (same way as last turn nodes were evaluated).  
Once every turn's outcome has received a rating the evaluation flag is set to DONE.  
![Alt text](./media/ex2.PNG?raw=true "Evaluation example")

## Choice to use MinMax 
The thought up game is faily light and fully evaluating each outcome does not take a lot of resources - a good choice for MinMax.
Alpha Beta would also be a good choice here but author did not choose it because of added complexity compared to MinMax.
Before committing to this game author considered making an algorithm for checkers and analyze each in depth of 2 proceeding turns.
However, complexity quickly became overwhelming for the time author had for this project both in terms of storing and updating game state and
creating the GUI for a game like this.
In fact even for this primitive game author made some mistakes with game state storage and processing which were not noticed unill testing and lead to sometimes confusing code and loss of time patching them out.

## Gameplay
Game is played using the generated game tree.  
Unlike evaluation, each turn is processed from top to bottom.  
Game is played by looping over the game tree two turns at a time.  
Each time the user presses fire/frost button, two turns in the game tree get processed - one turn from human input and the other for AI.  
In case of human input the corresponding spell is used to search the chosen outcome in th game tree*.  
In case of AI all turn's outcomes are evaluated - best rating is picked (rating = 1)  
In case both options have rating = 1 then AI additionally evaluates the two option's product (sum points).  
Preference is given to outcomes with smaller point product for opponent.  
![Alt text](./media/ex3.PNG?raw=true "Gameplay example")
![Alt text](./media/ex4.PNG?raw=true "Gameplay example GUI")
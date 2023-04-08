from Player import Player
from Game import Game
from TurnTree import TurnTree
from random import getrandbits

# Choose which player to play as
human_player: str = input("Choose player? [p1/p2]").lower()
valid_input: bool = False

while not valid_input:
    if human_player == 'p1' or human_player == 'p2':
        valid_input = True

    else:
        print(
            f'Answer needs to be p1 or p2, your answer was {human_player}')
        human_player = input(
            "Choose player? [p1/p2]").lower()

p1_is_ai: bool = False if human_player == 'p1' else True
p2_is_ai: bool = False if human_player == 'p2' else True

player_one = Player(ai=p1_is_ai)
player_two = Player(ai=p2_is_ai)

player_one_goes_first = bool(getrandbits(1))
player_one_turn: bool = False

# Initialize and generate every possible turn with the above settings
turn_tree = TurnTree(player_one=player_one,
              player_two=player_two,
              player_one_goes_first=player_one_goes_first)

# Store every turn outcome
turn_tree.generateTree()
turn_tree.evaluateTree()
turns: dict = turn_tree.getTree()

# Initialize the game
game = Game(player_one=player_one,
            player_two=player_two,
            turns=turns)

print(
    f'Initializing game\nPlayer one health = {player_one.getHealth()}, shields = {player_one.getShields()}\nPlayer two health = {player_two.getHealth()}, shields = {player_two.getShields()}')
print(f'You are playing as {human_player}')
print('____________________________________')

# Play the game
game.processFirstTurn()

while game.player_one.getHealth() > 0 and game.player_two.getHealth() > 0:

    game.processTurn()


if game.player_one.getHealth() > 0:
    print('Player one has won!')
else:
    print('Player two has won!')

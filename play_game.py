from Player import Player
from Game import Game
from TurnTree import TurnTree
from random import getrandbits

# Choose which player to play as
human_player: str = input("Choose player: [p1/p2]").lower()
valid_input: bool = False

while not valid_input:
    if human_player == 'p1' or human_player == 'p2':
        valid_input = True

    else:
        print(
            f'Answer needs to be p1 or p2, your answer was {human_player}')
        human_player = input(
            "Choose player? [p1/p2]").lower()

player_one = Player(ai=False if human_player == 'p1' else True)
player_two = Player(ai=False if human_player == 'p2' else True)

first_turn_player: str = player_one.firstTurnInput()
player_one_goes_first: bool = True if first_turn_player == 'p1' else False

# Initialize and generate every possible turn with the above settings
turn_tree = TurnTree(
    player_one=player_one,
    player_two=player_two,
    player_one_goes_first=player_one_goes_first)

# Store every turn outcome
turn_tree.generateTree()
turn_tree.evaluateTree()
turns: dict = turn_tree.getTree()


print(
    f'Initializing game\nPlayer one health = {player_one.getHealth()}, shields = {player_one.getShields()}\nPlayer two health = {player_two.getHealth()}, shields = {player_two.getShields()}')
print(f'You are playing as {human_player}')
print('____________________________________')

# Initialize game with params
game = Game(player=player_one, # doesnt matter which one, we just want the player class methods
            human_player=human_player,
            ai_player=turn_tree.ai_player,
            turns=turns,
            player_one_goes_first=player_one_goes_first)

# Play game
game.processFirstTurn()
while game.human_health > 0 and game.ai_health > 0:
    game.processTurn()

if game.human_health > 0:
    print('Human player has won!')
else:
    print('AI has won!')

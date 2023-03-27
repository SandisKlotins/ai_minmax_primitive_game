from Player import Player
from Game import Game
from min_max_tree import generateTurnTree
from random import getrandbits


player_one = Player(ai=False)
player_two = Player(ai=True)

game = Game(player_one, player_two)

player_one_goes_first = bool(getrandbits(1))
player_one_turn: bool = False

game_tree = generateTurnTree(
    minimizer=player_one, 
    maximizer=player_two, 
    minimizer_goes_first=player_one_goes_first
)

print(f'Initializing game\nPlayer one health = {player_one.health}, shields = {player_one.shields}\nPlayer two health = {player_two.health}, shields = {player_two.shields}')

game.processFirstTurn()
# Process following turns
while game.player_one.health > 0 and game.player_two.health > 0:
    game.processTurn()


if game.player_one.health > 0:
    print('Player one has won!')
else:
    print('Player two has won!')
from Player import Player
from Game import Game
from random import getrandbits


player_one = Player(ai=False)
player_two = Player(ai=True)

game = Game(player_one, player_two)

player_one_goes_first = bool(getrandbits(1))
player_one_turn: bool = False


print(
    f'Initializing game\nPlayer one health = {player_one.getHealth()}, shields = {player_one.getShields()}\nPlayer two health = {player_two.getHealth()}, shields = {player_two.getShields()}')

# Play the game
game.processFirstTurn()

while game.player_one.getHealth() > 0 and game.player_two.getHealth() > 0:

    game.processTurn()


if game.player_one.getHealth() > 0:
    print('Player one has won!')
else:
    print('Player two has won!')

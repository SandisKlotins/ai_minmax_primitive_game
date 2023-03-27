from Player import Player
from random import getrandbits
from math import ceil


def calcMaxNumTurns(
        minimizer_health: int, 
        minimizer_shields: int, 
        maximizer_health: int, 
        maximizer_shields: int, 
        min_dmg_shields: int, 
        min_dmg_health: int) -> int:
    
    minimizerMaxNumTurns: int = ceil(float(minimizer_health)/min_dmg_health) + ceil(float(minimizer_shields)/min_dmg_shields)
    maximizerMaxNumTurns: int = ceil(float(maximizer_health)/min_dmg_health) + ceil(float(maximizer_shields)/min_dmg_shields)

    return int(minimizerMaxNumTurns + maximizerMaxNumTurns - 1)


def generateTurnTree(minimizer: Player, maximizer: Player, minimizer_goes_first: bool):
    # Maximum number of turns the game can last if both players make the worst possible turns
    maxNumTurns: int = calcMaxNumTurns(
        minimizer_health=minimizer.health, 
        minimizer_shields=minimizer.shields, 
        maximizer_health=maximizer.health, 
        maximizer_shields=maximizer.shields, 
        min_dmg_shields=5, 
        min_dmg_health=5
    )

    return None


# player_one = Player(is_ai=False)
# player_two = Player(is_ai=True)

# player_one_goes_first = bool(getrandbits(1))

# game_tree = generateTurnTree(
#     minimizer=player_one, 
#     maximizer=player_two, 
#     minimizer_goes_first=player_one_goes_first
# )
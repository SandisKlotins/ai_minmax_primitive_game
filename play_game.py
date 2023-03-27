from Player import Player
from playerInput import playerInput
from min_max_tree import generateTurnTree
from random import randint, getrandbits


player_one = Player(is_ai=False)
player_two = Player(is_ai=True)

player_one_goes_first = bool(getrandbits(1))
is_first_turn: bool = True
player_one_turn: bool = False

game_tree = generateTurnTree(player_one, player_two, player_one_goes_first)

ai_dmg: int = 5
turn_num: int = 1

print(f'Initializing game\nPlayer one health = {player_one.health}, shields = {player_one.shields}\nPlayer two health = {player_two.health}, shields = {player_two.shields}')

while player_one.health > 0 and player_two.health > 0:
    # Porcess 1st turn
    if is_first_turn and player_one_goes_first:
        print('Player one goes first')
        if player_one.is_ai:
            player_two.health = player_two.health - ai_dmg
            player_one_turn = False
            is_first_turn = False
        else:
            spell_choice: str = playerInput()
            print(f'Player one attacks with {spell_choice}')
            dmg: dict = player_one.spellChoice(spell_choice, player_two.shields)
            player_two.health = player_two.health - dmg['health']
            player_two.shields = player_two.shields - dmg['shield']

            is_first_turn = False

        print('____________________________________')
        print(f'Player one health = {player_one.health}, shields = {player_one.shields}\nPlayer two health = {player_two.health}, shields = {player_two.shields}\nTurn {turn_num} concluded')
        print('____________________________________')

    elif is_first_turn:
        print('Player two goes first')
        player_one.health = player_one.health - ai_dmg
        player_one_turn = True
        is_first_turn = False

        print('____________________________________')
        print(f'Player one health = {player_one.health}, shields = {player_one.shields}\nPlayer two health = {player_two.health}, shields = {player_two.shields}\nTurn {turn_num} concluded')
        print('____________________________________')
    
    # Process regular turn
    if not is_first_turn and player_one_turn:
        print('Player one turn')
        player_two.health = player_two.health - ai_dmg
        player_one_turn = False
    elif not is_first_turn:
        print('Player two turn')
        player_one.health = player_one.health - ai_dmg
        player_one_turn = True
    
    turn_num = turn_num + 1
    print(f'Player one health = {player_one.health}, shields = {player_one.shields}\nPlayer two health = {player_two.health}, shields = {player_two.shields}\nTurn {turn_num} concluded')
    print('____________________________________')


if player_one.health > 0:
    print('Player one has won!')
else:
    print('Player two has won!')
from Player import Player
# from Game import Game
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

# Initialize game params
# Keeps track of turn
turn: int = 0
# Keep tack of which choice lead to current turn (used for ai turn evaluation)
previous_id: int = turns[turn][0]['id']
human_health: int
ai_health: int
# Set game to start on 1st turn (1st choice)
turn = turn + 1

# Play out first turn
options: list[dict] = turns[turn]
# Process AI turn
if options[0]['player'] == turn_tree.ai_player:
    # Set default as bad option
    max_rating: int = -1
    # If there are no good options use the first element in the list
    best_option: dict = options[0]

    for option in options:
        if max_rating < option['rating']:
            max_rating = option['rating']
            best_option = option

        # Subroutine: in case ai values its best option and the current option the same.
        # Check if options product is better. This helps AI make overall better choices if the human player is not playing optimally
        elif max_rating == option['rating']:
            option_product: int = option[human_player]['health'] + option[human_player]['shields']
            best_option_product: int = best_option[human_player]['health'] + best_option[human_player]['shields']

            if option_product < best_option_product:
                best_option = option

    spell: str = best_option['spell']
    human_health = best_option[human_player]['health']
    ai_health = best_option[turn_tree.ai_player]['health']
    previous_id = best_option['id']


else:
    # Process human turn
    spell: str = player_one.input()
    option: dict = [node for node in turns[turn] if node['spell'] == spell][0]
    human_health = option[human_player]['health']
    ai_health = option[turn_tree.ai_player]['health']
    previous_id = option['id']

turn = turn + 1

# Play out remaining turns
while human_health > 0 and ai_health > 0:

    options: list[dict] = [option for option in turns[turn] if previous_id in option['previous_id']]
    # Process AI turn
    if options[0]['player'] == turn_tree.ai_player:
        # Set default as bad option
        max_rating: int = -1
        # If there are no good options use the first element in the list
        best_option: dict = options[0]

        for option in options:
            if max_rating < option['rating']:
                max_rating = option['rating']
                best_option = option

            # Subroutine: in case ai values its best option and the current option the same.
            # Check if options product is better. This helps AI make overall better choices if the human player is not playing optimally
            elif max_rating == option['rating']:
                option_product: int = option[human_player]['health'] + option[human_player]['shields']
                best_option_product: int = best_option[human_player]['health'] + best_option[human_player]['shields']

                if option_product < best_option_product:
                    best_option = option

        spell: str = best_option['spell']
        human_health = best_option[human_player]['health']
        ai_health = best_option[turn_tree.ai_player]['health']
        previous_id = best_option['id']

        print(previous_id)
        print(option)


    else:
        # Process human turn
        spell: str = player_one.input()
        option: dict = [node for node in turns[turn] if node['spell'] == spell][0]
        human_health = option[human_player]['health']
        ai_health = option[turn_tree.ai_player]['health']
        previous_id = option['id']

        print(previous_id)
        print(option)

    turn = turn + 1

if human_health > 0:
    print('Human player has won!')
else:
    print('AI has won!')

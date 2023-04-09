from Player import Player
from random import getrandbits
from math import ceil
from sys import exit
import time


class TurnTree:
    def __init__(self,
                 player_one: Player,
                 player_two: Player,
                 player_one_goes_first: bool):
        self.player_one: Player = player_one
        self.player_two: Player = player_two
        self.turn: int = 0
        self.player_one_goes_first: bool = player_one_goes_first
        self.state: dict = {}
        self.ai_player: str = 'p1' if self.player_one.isAi() else 'p2'
        self.ai_opponent: str = 'p2' if self.player_one.isAi() else 'p1'
        self.node_id: int = 0
        self.__is_evaluated: bool = False

    def __generateRootNode(self) -> None:
        # Add root node
        if not self.turn == 0:
            exit(
                f'Cannot create root node. Turn must be 0 | turn = {self.turn}')

        print('Adding root node...')
        # Root node is not actually a turn so we set it to player who does not make the turn
        # Meaning on turn 1 the real turn 1 player will do the turn
        players_turn = 'p2' if self.player_one_goes_first else 'p1'

        self.state[self.turn] = [{
            'id': self.node_id,
            'previous_id': {0},
            'p1': {'health': self.player_one.getHealth(), 'shields': self.player_one.getShields()},
            'p2': {'health': self.player_two.getHealth(), 'shields': self.player_two.getShields()},
            'player': players_turn,
            'spell': '',
            'rating': 0}]

        self.node_id = self.node_id + 1
        print(
            f'Turn {self.turn} number of nodes: {len(self.state)}')
        self.turn = self.turn + 1

    # Updates state with all possible outcomes based on previous turn

    def __generateNextTurn(self) -> None:
        if len(self.state) == 0:
            self.__generateRootNode()

        # Store all outcomes of current turn
        turn_nodes: list = []

        # Set used to check for duplicate nodes
        seen: list = list()

        # Iterate over all the outcomes from the previous turn.
        # For each outcome generate 2 possible outcomes -
        # result of fire or frost attack
        for node in self.state[self.turn - 1]:
            # Determine which player makes the turn
            players_turn = 'p1' if node['player'] == 'p2' else 'p2'

            # Determine which player will be attacked
            opponent = 'p2' if node['player'] == 'p2' else 'p1'

            # Process attack damage
            fire_dmg: dict = self.player_one.spellChoice(
                'fire', node[opponent]['shields'])
            frost_dmg: dict = self.player_one.spellChoice(
                'frost', node[opponent]['shields'])

            # Process fire attack
            player_health = node[players_turn]['health']
            player_shields = node[players_turn]['shields']
            opponent_health = node[opponent]['health'] - fire_dmg['health']
            opponent_shields = node[opponent]['shields'] - fire_dmg['shields']

            # Stores each nodes fingerprint
            node_vals: tuple = (player_health, player_shields,
                                opponent_health, opponent_shields)

            # Only append nodes where player or opponent health is non negative
            # Already dead players cant attack and already dead opponents cant reveive more damage
            # Avoid duplicate nodes (same health/shields combinations for opponent and player)
            if (not player_health <= 0 and not node[opponent]['health'] <= 0):
                if node_vals not in seen:
                    turn_nodes.append({
                        'id': self.node_id,
                        'previous_id': {node['id']},
                        players_turn: {'health': player_health, 'shields': player_shields},
                        opponent: {'health': opponent_health, 'shields': opponent_shields},
                        'player': players_turn,
                        'spell': 'fire',
                        'rating': None})

                    self.node_id = self.node_id + 1
                    seen.append(node_vals)

                else:

                    # If a node with those values already exists update possible paths to get to that node
                    node_idx = seen.index(node_vals)
                    turn_nodes[node_idx]['previous_id'].add(node['id'])

            # Process frost attack
            player_health = node[players_turn]['health']
            player_shields = node[players_turn]['shields']
            opponent_health = node[opponent]['health'] - frost_dmg['health']
            opponent_shields = node[opponent]['shields'] - frost_dmg['shields']

            node_vals: tuple = (player_health, player_shields,
                                opponent_health, opponent_shields)

            if (not player_health <= 0 and not node[opponent]['health'] <= 0):
                if node_vals not in seen:
                    turn_nodes.append({
                        'id': self.node_id,
                        'previous_id': {node['id']},
                        players_turn: {'health': player_health, 'shields': player_shields},
                        opponent: {'health': opponent_health, 'shields': opponent_shields},
                        'player': players_turn,
                        'spell': 'frost',
                        'rating': None})

                    self.node_id = self.node_id + 1
                    seen.append(node_vals)

                else:

                    node_idx = seen.index(node_vals)
                    turn_nodes[node_idx]['previous_id'].add(node['id'])

        print(
            f'Turn {self.turn} number of nodes: {len(turn_nodes)}')

        # Save the turn in state
        self.state[self.turn] = turn_nodes
        self.turn = self.turn + 1

    def generateTree(self):
        self.__generateRootNode()
        while not len(self.state[self.turn - 1]) == 0:
            self.__generateNextTurn()

        # Last turn will always be empty, remove it.
        del self.state[self.turn - 1]

        self.turn = self.turn - 2
        print(f'Max turn set to {self.turn}!\n')

    def getTree(self) -> dict:
        num_turns: int = len(self.state)

        if num_turns > 0 and self.__is_evaluated:
            return self.state

        exit(
            f'No turns have yet been generated OR evaluated, cannot return sate | turns = {num_turns}')

    def evaluateTree(self) -> None:
        if len(self.state) == 0:
            exit('Game tree has not been generated yet.')

        while self.turn != 0:
            # Prep
            next_turn_outcomes: list[tuple] = []
            next_turn_ids: list[int] = []

            # Esure list index is not out of range
            if not self.turn == len(self.state) - 1:
                next_turn_outcomes: dict = {previous_id: node['rating'] for node in self.state[self.turn + 1] for previous_id in node['previous_id']}
                next_turn_ids: set[int] = {previous_id for id_set in self.state[self.turn + 1] for previous_id in id_set['previous_id']}

            for node in range(len(self.state[self.turn])):
                # Check if node spawn more turns
                if self.state[self.turn][node]['id'] not in next_turn_ids:

                    # If node id is not present in next turn then it's a dead end node, assign new rating.
                    rating: int = 1 if self.state[self.turn][node][self.ai_opponent]['health'] <= 0 else -1
                    self.state[self.turn][node]['rating'] = rating

                else:
                    # Use next turns rating
                    rating: int = next_turn_outcomes[self.state[self.turn][node]['id']]
                    self.state[self.turn][node]['rating'] = rating

            self.turn = self.turn - 1
        self.__is_evaluated = True


# player_one = Player(ai=False)
# player_two = Player(ai=True)

# player_one_goes_first = bool(getrandbits(1))
# player_one_turn: bool = False

# # Initialize and generate every possible turn with the above settings
# turn_tree = TurnTree(player_one=player_one,
#                      player_two=player_two,
#                      player_one_goes_first=player_one_goes_first)

# turn_tree.generateTree()
# turn_tree.evaluateTree()

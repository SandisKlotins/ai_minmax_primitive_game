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
        self.player_one = player_one
        self.player_two = player_two
        self.turn: int = 0
        self.player_one_goes_first = player_one_goes_first
        self.state: dict = {}
        self.ai_player = 'p1' if self.player_one.isAi() else 'p2'
        self.ai_opponent = 'p2' if self.player_one.isAi() else 'p1'


    def __generateRootNode(self) -> None:
        # Add root node
        if not self.turn == 0:
            exit(
                f'Cannot create root node. Turn must be 0 | turn = {self.turn}')

        print('Adding root node...')
        players_turn = 'p1' if self.player_one_goes_first else 'p2'

        self.state[self.turn] = [{
            'p1': {'health': self.player_one.getHealth(), 'shields': self.player_one.getShields()},
            'p2': {'health': self.player_two.getHealth(), 'shields': self.player_two.getShields()},
            'player': players_turn,
            'spell': '',
            'rating': 0}]

        self.turn = self.turn + 1


    # Updates state with all possible outcomes based on previous turn
    def __generateNextTurn(self) -> None:
        if len(self.state) == 0:
            self.__generateRootNode()

        # print(f'Generating all possible turns for turn {self.turn}')

        # Store all outcomes of current turn
        turn_nodes = []

        # Set used to check for duplicate nodes
        seen = set()

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
            node_vals: tuple = (player_health, player_shields, opponent_health, opponent_shields)

            # Only append nodes where player or opponent health is non negative
            # Already dead players cant attack and already dead opponents cant reveive more damage
            # Avoid duplicate nodes (same health/shields combinations for opponent and player)
            if (not player_health <= 0 and not node[opponent]['health'] <= 0) and node_vals not in seen:
                turn_nodes.append({
                    players_turn: {'health': player_health, 'shields': player_shields},
                    opponent: {'health': opponent_health, 'shields': opponent_shields},
                    'player': players_turn,
                    'spell': 'fire',
                    'rating': 0})
                
                seen.add(node_vals)

            # Process frost attack
            player_health = node[players_turn]['health']
            player_shields = node[players_turn]['shields']
            opponent_health = node[opponent]['health'] - frost_dmg['health']
            opponent_shields = node[opponent]['shields'] - frost_dmg['shields']

            node_vals: tuple = (player_health, player_shields, opponent_health, opponent_shields)

            if (not player_health <= 0 and not node[opponent]['health'] <= 0) and node_vals not in seen:
                turn_nodes.append({
                    players_turn: {'health': player_health, 'shields': player_shields},
                    opponent: {'health': opponent_health, 'shields': opponent_shields},
                    'player': players_turn,
                    'spell': 'frost',
                    'rating': 0})
                
                seen.add(node_vals)

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

        if num_turns > 0:
            return self.state

        exit(f'No turns have yet been generated, cannot return sate | turns = {num_turns}')


    def __evaluateLastTurn(self):
        print(f'{self.ai_player} is ai player')

        for i in range(len(self.state[self.turn])):
            # If opponent is dead, rating is positive else negative
            rating = 1 if self.state[self.turn][i][self.ai_opponent]['health'] <= 0 else -1
            self.state[self.turn][i]['rating'] = rating
            
    # <toDo> figure out how to link nodes between turns
    def evaluateTree(self):
        if len(self.state) == 0:
            exit('Game tree has not been generated yet.')

        # Assigns rating to all last turn nodes
        self.__evaluateLastTurn()


player_one = Player(ai=True)
player_two = Player(ai=False)

player_one_goes_first = bool(getrandbits(1))
player_one_turn: bool = False

# Initialize and generate every possible turn with the above settings
turn_tree = TurnTree(player_one=player_one,
              player_two=player_two,
              player_one_goes_first=player_one_goes_first)

turn_tree.generateTree()
turn_tree.evaluateTree()

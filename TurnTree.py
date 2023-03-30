from Player import Player
from random import getrandbits
from math import ceil
from sys import exit


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
        self.done: bool = False

    def incrementTurn(self) -> None:
        self.turn = self.turn + 1

    def generateRootNode(self) -> None:
        # Add root node
        if not self.turn == 0:
            exit(f'Cannot create root node. Turn must be 0 | turn = {self.turn}')

        print('Adding root node...')
        players_turn = 'p1' if self.player_one_goes_first else 'p2'

        print(f'{players_turn} turn')
        self.state[self.turn] = [{
            'p1': {'health': self.player_one.getHealth(), 'shields': self.player_one.getShields()},
            'p2': {'health': self.player_two.getHealth(), 'shields': self.player_two.getShields()},
            'player': players_turn,
            'spell': '',
            'rating': 0}]
        self.incrementTurn()


    # Updates state with all possible outcomes based on previous tunr
    def generateNextTurn(self) -> None:
        if len(self.state) == 0:
            self.generateRootNode()

        print(f'Generating all possible turns for turn {self.turn}')

        # Initialize a new list to store all outcomes of current turn
        self.state[self.turn] = []

        # Iterate over all the outcomes from the previous turn.
        # For each outcome generate 2 possible outcomes -
        # result of fire or frost attack
        for node in self.state[self.turn - 1]:
            
            # Determine which player makes the turn
            players_turn = 'p1' if node['player'] == 'p2' else 'p2'

            # Determine which player will be attacked
            opponent = 'p2' if node['player'] == 'p2' else 'p1'

            # Get opponents health and shields and process attack damage
            fire_dmg: dict = self.player_one.spellChoice('fire', node[opponent]['shields'])
            frost_dmg: dict = self.player_one.spellChoice('frost', node[opponent]['shields'])

            # Process fire attack
            self.state[self.turn].append({
                players_turn: {'health': node[players_turn]['health'], 'shields': node[players_turn]['shields']},
                opponent: {'health': node[opponent]['health'] - fire_dmg['health'], 'shields': node[opponent]['shields']},
                'player': players_turn,
                'spell': 'fire',
                'rating': 0})
            
            # Process frost attack
            self.state[self.turn].append({
                players_turn: {'health': node[players_turn]['health'], 'shields': node[players_turn]['shields']},
                opponent: {'health': node[opponent]['health'] - frost_dmg['health'], 'shields': node[opponent]['shields'] - frost_dmg['shields']},
                'player': players_turn,
                'spell': 'frost',
                'rating': 0})
        print(self.state[self.turn])
        self.incrementTurn()
    
    def test(self):
        self.generateNextTurn() # 1
        self.generateNextTurn() # 2
        self.generateNextTurn() # 3
        self.generateNextTurn() # 4
        self.generateNextTurn() # 5
        self.generateNextTurn() # 6
        self.generateNextTurn() # 7
        self.generateNextTurn() # 8
        self.generateNextTurn() # 9
        self.generateNextTurn() # 10
        self.generateNextTurn() # 11
        self.generateNextTurn() # 12
        self.generateNextTurn() # 13
        self.generateNextTurn() # 14
        self.generateNextTurn() # 15
        self.generateNextTurn() # 16
        self.generateNextTurn() # 17
        self.generateNextTurn() # 18
        self.generateNextTurn() # 19
        self.generateNextTurn() # 20
        self.generateNextTurn() # 21



player_one = Player(ai=False)
player_two = Player(ai=True)
player_one_goes_first = bool(getrandbits(1))

tt = TurnTree(player_one=player_one,
              player_two=player_two,
              player_one_goes_first=player_one_goes_first)

tt.test()
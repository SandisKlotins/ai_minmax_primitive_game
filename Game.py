from random import getrandbits
from Player import Player


class Game:
    def __init__(self, player_one: Player, player_two: Player, turns: dict):
        self.player_one = player_one
        self.player_two = player_two
        self.turn: int = 0
        self.player_one_goes_first = bool(getrandbits(1))
        self.player_one_turn: bool = False
        self.turns = turns

    def aiBestOption(self) -> str:

        options: list[dict] = self.turns[self.turn + 1]
        max_rating: int = -1

        # Debug
        print(options)
        # In case there are no better options pick the first option in the list
        best_option: dict = self.turns[self.turn + 1][0]

        opponent: str = 'p2' if self.player_one.isAi() else 'p1'

        # Pick the highest rated turn
        for option in range(len(options)):
            if max_rating < options[option]['rating']:

                max_rating = options[option]['rating']
                best_option = options[option]

            # Subroutine to further optimize result when multiple nodes have the same rating
            # Some nodes can still have a smaller product despite the rating
            elif max_rating == options[option]['rating']:
                if options[option][opponent]['health'] + options[option][opponent]['shields'] < best_option[opponent]['health'] + best_option[opponent]['shields']:
                    max_rating = options[option]['rating']
                    best_option = options[option]

        return best_option['spell']

    def processFirstTurn(self) -> None:
        if self.player_one_goes_first:
            print('Player one goes first')
            if self.player_one.isAi():
                spell_choice: str = self.aiBestOption()

                print(f'Player one attacks with {spell_choice}')
                dmg: dict = self.player_one.spellChoice(
                    spell_choice, self.player_two.getShields())
                self.player_two.setHealth(
                    self.player_two.getHealth() - dmg['health'])
                self.player_two.setShields(
                    self.player_two.getShields() - dmg['shields'])

            else:
                spell_choice: str = self.player_one.input()
                print(f'Player one attacks with {spell_choice}')
                dmg: dict = self.player_one.spellChoice(
                    spell_choice, self.player_two.getShields())
                self.player_two.setHealth(
                    self.player_two.getHealth() - dmg['health'])
                self.player_two.setShields(
                    self.player_two.getShields() - dmg['shields'])

            self.player_one_turn = False

        else:
            print('Player two goes first')
            if self.player_two.isAi():
                spell_choice: str = self.aiBestOption()

                print(f'Player two attacks with {spell_choice}')
                dmg: dict = self.player_two.spellChoice(
                    spell_choice, self.player_one.getShields())
                self.player_one.setHealth(
                    self.player_one.getHealth() - dmg['health'])
                self.player_one.setShields(
                    self.player_one.getShields() - dmg['shields'])

            else:
                spell_choice: str = self.player_two.input()
                print(f'Player one attacks with {spell_choice}')
                dmg: dict = self.player_two.spellChoice(
                    spell_choice, self.player_two.getShields())
                self.player_one.setHealth(
                    self.player_one.getHealth() - dmg['health'])
                self.player_one.setShields(
                    self.player_one.getShields() - dmg['shields'])

            self.player_one_turn = True

        self.turn = self.turn + 1
        print('____________________________________')
        print(f'Player one health = {self.player_one.getHealth()}, shields = {self.player_one.getShields()}\nPlayer two health = {self.player_two.getHealth()}, shields = {self.player_two.getShields()}\nTurn {self.turn} concluded')
        print('____________________________________')

    def processTurn(self) -> None:
        if self.player_one_turn:
            print('Player one turn')
            if self.player_one.isAi():
                spell_choice: str = self.aiBestOption()

                print(f'Player two attacks with {spell_choice}')
                dmg: dict = self.player_one.spellChoice(
                    spell_choice, self.player_two.getShields())
                self.player_two.setHealth(
                    self.player_two.getHealth() - dmg['health'])
                self.player_two.setShields(
                    self.player_two.getShields() - dmg['shields'])

            else:
                spell_choice: str = self.player_one.input()
                print(f'Player one attacks with {spell_choice}')
                dmg: dict = self.player_one.spellChoice(
                    spell_choice, self.player_two.getShields())
                self.player_two.setHealth(
                    self.player_two.getHealth() - dmg['health'])
                self.player_two.setShields(
                    self.player_two.getShields() - dmg['shields'])

            self.player_one_turn = False

        else:
            print('Player two turn')
            if self.player_two.isAi():

                spell_choice: str = self.aiBestOption()
                print(f'Player two attacks with {spell_choice}')
                dmg: dict = self.player_two.spellChoice(
                    spell_choice, self.player_one.getShields())
                self.player_one.setHealth(
                    self.player_one.getHealth() - dmg['health'])
                self.player_one.setShields(
                    self.player_one.getShields() - dmg['shields'])

            else:
                spell_choice: str = self.player_two.input()
                print(f'Player two attacks with {spell_choice}')
                dmg: dict = self.player_two.spellChoice(
                    spell_choice, self.player_one.getShields())
                self.player_one.setHealth(
                    self.player_one.getHealth() - dmg['health'])
                self.player_one.setShields(
                    self.player_one.getShields() - dmg['shields'])

            self.player_one_turn = True

        self.turn = self.turn + 1
        print(f'Player one health = {self.player_one.getHealth()}, shields = {self.player_one.getShields()}\nPlayer two health = {self.player_two.getHealth()}, shields = {self.player_two.getShields()}\nTurn {self.turn} concluded')
        print('____________________________________')

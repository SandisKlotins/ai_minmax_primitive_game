from random import getrandbits
from Player import Player


class Game:
    def __init__(self, player_one: Player, player_two: Player):
        self.player_one = player_one
        self.player_two = player_two
        self.turn: int = 1
        self.player_one_goes_first = bool(getrandbits(1))
        self.player_one_turn: bool = False

    def incrementTurn(self) -> None:
        self.turn = self.turn + 1

    def processFirstTurn(self) -> None:
        if self.player_one_goes_first:
            print('Player one goes first')
            if self.player_one.isAi():
                self.player_two.setHealth(
                    self.player_two.getHealth() - self.player_one.getAiDmg())

            else:
                spell_choice: str = self.player_one.input()
                print(f'Player one attacks with {spell_choice}')
                dmg: dict = self.player_one.spellChoice(
                    spell_choice, self.player_two.getShields())
                self.player_two.setHealth(
                    self.player_two.getHealth() - dmg['healths'])
                self.player_two.setShields(
                    self.player_two.getShields() - dmg['shields'])

            self.player_one_turn = False

        else:
            print('Player two goes first')
            if self.player_two.isAi():
                self.player_one.setHealth(
                    self.player_one.getHealth() - self.player_two.getAiDmg())

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

        self.incrementTurn()
        print('____________________________________')
        print(f'Player one health = {self.player_one.getHealth()}, shields = {self.player_one.getShields()}\nPlayer two health = {self.player_two.getHealth()}, shields = {self.player_two.getShields()}\nTurn {self.turn} concluded')
        print('____________________________________')

    def processTurn(self) -> None:
        if self.player_one_turn:
            print('Player one turn')
            self.player_two.setHealth(
                self.player_two.getHealth() - self.player_one.getAiDmg())
            self.player_one_turn = False
        else:
            print('Player two turn')
            self.player_one.setHealth(
                self.player_one.getHealth() - self.player_two.getAiDmg())
            self.player_one_turn = True

        self.incrementTurn()
        print(f'Player one health = {self.player_one.getHealth()}, shields = {self.player_one.getShields()}\nPlayer two health = {self.player_two.getHealth()}, shields = {self.player_two.getShields()}\nTurn {self.turn} concluded')
        print('____________________________________')

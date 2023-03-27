from random import getrandbits
from Player import Player

class Game:
    def __init__(self, player_one: Player, player_two: Player):
        self.player_one = player_one
        self.player_two = player_two,
        self.turn: int = 1,
        self.player_one_goes_first = bool(getrandbits(1))
        self.player_one_turn: bool

    def incrementTurn(self):
        self.turn = self.turn + 1

    def processFirstTurn(self):
        if self.player_one_goes_first:
            print('Player one goes first')
            if self.player_one.is_ai():
                self.player_two.set_health(self.player_two.get_health() - self.player_one.get_ai_dmg())

            else:
                spell_choice: str = self.player_one.input()
                print(f'Player one attacks with {spell_choice}')
                dmg: dict = self.player_one.spellChoice(spell_choice, self.player_two.get_shields())
                self.player_two.set_health(self.player_two.get_health() - dmg['health'])
                self.player_two.set_shields(self.player_two.get_shields() - dmg['shield'])

            self.player_one_turn = False

        else:
            print('Player two goes first')
            if self.player_two.is_ai():
                self.player_one.set_health(self.player_one.get_health() - self.player_two.get_ai_dmg())

            else:
                spell_choice: str = self.player_two.input()
                print(f'Player one attacks with {spell_choice}')
                dmg: dict = self.player_two.spellChoice(spell_choice, self.player_two.get_shields())
                self.player_one.set_health(self.player_one.get_health() - dmg['health'])
                self.player_one.set_shields(self.player_one.get_shields() - dmg['shield'])

            self.player_one_turn = True

        self.incrementTurn()
        print('____________________________________')
        print(f'Player one health = {self.player_one.get_health()}, shields = {self.player_one.get_shields()}\nPlayer two health = {self.player_two.get_health()}, shields = {self.player_two.get_shields()}\nTurn {self.turn} concluded')
        print('____________________________________')

    def processTurn(self):
        if self.player_one_turn:
            print('Player one turn')
            self.player_two.set_health(self.player_two.get_health() - self.player_one.get_ai_dmg())
            self.player_one_turn = False
        else :
            print('Player two turn')
            self.player_one.set_health(self.player_one.get_health() - self.player_two.get_ai_dmg())
            self.player_one_turn = True
        
        self.incrementTurn()
        print(f'Player one health = {self.player_one.get_health()}, shields = {self.player_one.get_shields()}\nPlayer two health = {self.player_two.get_health()}, shields = {self.player_two.get_shields()}\nTurn {self.turn} concluded')
        print('____________________________________')

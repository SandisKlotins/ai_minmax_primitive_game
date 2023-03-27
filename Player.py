from random import randint

class Player:
    def __init__(self, ai: bool):
        self.ai = ai
        self.health: int = randint(30, 60)
        self.shields: int = 100 - self.health
        self.ai_dmg: int = 5

    def is_ai(self) -> bool:
        return self.ai
    
    def get_shields(self) -> int:
        return self.shields

    def get_health(self) -> int:
        return self.health
    
    def get_ai_dmg(self) -> int:
        return self.ai_dmg

    def set_shields(self, shields):
        self.shields = shields

    def set_health(self, health):
        self.health = health

    def set_ai_dmg(self, ai_dmg):
        self.ai_dmg = ai_dmg

    def castFireBolt(self, opponents_shield: int) -> dict:
        if opponents_shield > 0:
            return {'health': 5, 'shield': 5}

        else:
            return {'health': 10, 'shield': 0}

    def castFrostBolt(self) -> dict:
        return {'health': 0, 'shield': 10}


    def input(self) -> str:
        spell_choice: str = input("Which spell to cast? [fire/frost]").lower()
        valid_input: bool = False

        while not valid_input:
            if spell_choice == 'fire' or spell_choice == 'frost':
                valid_input = True
            else:
                print(f'Answer needs to be fire or frost, your answer was {spell_choice}')
                spell_choice = input("Which spell to cast? [fire/frost]").lower()

        return spell_choice


    def spellChoice(self, spell_choice: str, opponents_shield: int) -> dict:
        if spell_choice == 'fire':
            return self.castFireBolt(opponents_shield)
            
        elif spell_choice == 'frost':
            return self.castFrostBolt()

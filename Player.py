from random import randint

class Player:
    def __init__(self, is_ai: bool):
        self.is_ai = is_ai
        self.health: int = randint(30, 60)
        self.shields: int = 100 - self.health

    def castFireBolt(self, opponents_shield: int) -> dict:
        if opponents_shield > 0:
            return {'health': 5, 'shield': 5}

        else:
            print(opponents_shield)
            return {'health': 10, 'shield': 0}

    def castFrostBolt(self) -> dict:
        return {'health': 0, 'shield': 10}

    def spellChoice(self, spell_choice: str, opponents_shield: int) -> dict:
        if spell_choice == 'fire':
            return self.castFireBolt(opponents_shield)
            
        elif spell_choice == 'frost':
            return self.castFrostBolt()

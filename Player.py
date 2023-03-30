from random import randint


class Player:
    def __init__(self, ai: bool):
        self.__ai = ai
        self.__health: int = randint(30, 60)
        self.__shields: int = 100 - self.__health
        self.__ai_dmg: int = 5

    def castFireBolt(self, opponents_shield: int) -> dict:
        if opponents_shield > 0:
            return {'health': 5, 'shields': 5}

        else:
            return {'health': 10, 'shields': 0}

    def castFrostBolt(self) -> dict:
        return {'health': 0, 'shields': 10}

    def input(self) -> str:
        spell_choice: str = input("Which spell to cast? [fire/frost]").lower()
        valid_input: bool = False

        while not valid_input:
            if spell_choice == 'fire' or spell_choice == 'frost':
                valid_input = True
            else:
                print(
                    f'Answer needs to be fire or frost, your answer was {spell_choice}')
                spell_choice = input(
                    "Which spell to cast? [fire/frost]").lower()

        return spell_choice

    def spellChoice(self, spell_choice: str, opponents_shield: int) -> dict:
        if spell_choice == 'fire':
            return self.castFireBolt(opponents_shield)

        elif spell_choice == 'frost':
            return self.castFrostBolt()

    def isAi(self) -> bool:
        return self.__ai

    def getShields(self) -> int:
        return self.__shields

    def getHealth(self) -> int:
        return self.__health

    def getAiDmg(self) -> int:
        return self.__ai_dmg

    def setAiDmg(self, ai_dmg) -> None:
        self.__ai_dmg = ai_dmg

    def setShields(self, shields) -> None:
        self.__shields = shields

    def setHealth(self, health) -> None:
        self.__health = health

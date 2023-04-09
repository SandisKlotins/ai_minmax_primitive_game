from random import randint


class Player:
    def __init__(self, ai: bool):
        self.__ai = ai
        self.__health: int = randint(40, 60)
        self.__shields: int = 80 - self.__health
        self.__ai_dmg: int = 5


    def castFireBolt(self, opponents_shield: int) -> dict:
        if opponents_shield > 0:
            return {'health': 5, 'shields': 5}

        else:
            return {'health': 10, 'shields': 0}


    def castFrostBolt(self, opponents_shield: int) -> dict:
        if opponents_shield > 0:
            return {'health': 0, 'shields': 15}

        else:
            return {'health': 5, 'shields': 0}


    def input(self) -> str:
        spell_choice: str = input("Which spell to cast? [fire/frost]").lower().strip()
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

    def firstTurnInput(self) -> str:
        first_turn_player: str = input("Which player will go first? [p1/p2]").lower().strip()
        valid_input: bool = False

        while not valid_input:
            if first_turn_player == 'p1' or first_turn_player == 'p2':
                valid_input = True
                
            else:
                print(
                    f'Answer needs to be p1 or p2, your answer was {first_turn_player}')
                first_turn_player = input(
                    "Which player will go first? [p1/p2]").lower().strip()

        return first_turn_player

    def spellChoice(self, spell_choice: str, opponents_shield: int) -> dict:
        if spell_choice == 'fire':
            return self.castFireBolt(opponents_shield)

        elif spell_choice == 'frost':
            return self.castFrostBolt(opponents_shield)


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

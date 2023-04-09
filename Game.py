from Player import Player

class Game:
    def __init__(self, 
                 player: Player,
                 human_player: str, 
                 ai_player: str, 
                 turns: dict, 
                 player_one_goes_first: bool):
        self.player = player
        self.human_player = human_player
        self.ai_player = ai_player
        self.player_one_goes_first = player_one_goes_first
        self.turns = turns
        self.turn: int = 0
        self.previous_id: int = 0
        self.human_health: int
        self.human_shields: int
        self.ai_health: int
        self.ai_shields: int

    def processFirstTurn(self) -> None:
        # Play out first turn
        # Set game to start on 1st turn (1st choice)
        self.turn = self.turn + 1
        print(self.turn)

        options: list[dict] = self.turns[self.turn]

        # Process AI turn
        if options[0]['player'] == self.ai_player:
            # Set default option rating
            # # If there are no good options use the first element in the list
            max_rating: int = -1
            best_option: dict = options[0]

            for option in options:
                if max_rating < option['rating']:
                    max_rating = option['rating']
                    best_option = option

                # Subroutine: in case ai values its best option and the current option the same
                # Check if options product is better. This helps AI make overall better choices if the human player is not playing optimally
                elif max_rating == option['rating']:
                    option_product: int = option[self.human_player]['health'] + option[self.human_player]['shields']
                    best_option_product: int = best_option[self.human_player]['health'] + best_option[self.human_player]['shields']

                    if option_product < best_option_product:
                        best_option = option

            spell: str = best_option['spell']
            self.human_health = best_option[self.human_player]['health']
            self.human_shields = best_option[self.human_player]['shields']
            self.ai_health = best_option[self.ai_player]['health']
            self.ai_shields = best_option[self.ai_player]['shields']
            self.previous_id = best_option['id']

        else:
            # Process human turn
            spell: str = self.player.input()
            option: dict = [node for node in self.turns[self.turn] if node['spell'] == spell][0]
            self.human_health = option[self.human_player]['health']
            self.human_shields = option[self.human_player]['shields']
            self.ai_health = option[self.ai_player]['health']
            self.ai_shields = option[self.ai_player]['shields']
            self.previous_id = option['id']

        print('____________________________________')
        print(f'Human health = {self.human_health}, shields = {self.human_shields}\nAI health = {self.ai_health}, shields = {self.ai_shields}\nTurn {self.turn} concluded')
        print('____________________________________')

        self.turn = self.turn + 1
        print(self.turn)

    def processTurn(self) -> None:
        # Play out regular turn
        print(self.previous_id)
        print(self.turns[self.turn])

        options: list[dict] = [option for option in self.turns[self.turn] if self.previous_id in option['previous_id']]

        # Process AI turn
        if options[0]['player'] == self.ai_player:
            # Set default as bad option
            max_rating: int = -1
            # If there are no good options use the first element in the list
            best_option: dict = options[0]

            for option in options:
                if max_rating < option['rating']:
                    max_rating = option['rating']
                    best_option = option

                # Subroutine: in case ai values its best option and the current option the same.
                # Check if options product is better. This helps AI make overall better choices if the human player is not playing optimally
                elif max_rating == option['rating']:
                    option_product: int = option[self.human_player]['health'] + option[self.human_player]['shields']
                    best_option_product: int = best_option[self.human_player]['health'] + best_option[self.human_player]['shields']

                    if option_product < best_option_product:
                        best_option = option

            spell: str = best_option['spell']
            self.human_health = best_option[self.human_player]['health']
            self.human_shields = best_option[self.human_player]['shields']
            self.ai_health = best_option[self.ai_player]['health']
            self.ai_shields = best_option[self.ai_player]['shields']
            self.previous_id = best_option['id']

        else:
            # Process human turn
            spell: str = self.player.input()
            option: dict = [node for node in self.turns[self.turn] if node['spell'] == spell][0]
            self.human_health = option[self.human_player]['health']
            self.human_shields = option[self.human_player]['shields']
            self.ai_health = option[self.ai_player]['health']
            self.ai_shields = option[self.ai_player]['shields']
            self.previous_id = option['id']

        print(f'Human health = {self.human_health}, shields = {self.human_shields}\nAI health = {self.ai_health}, shields = {self.ai_shields}\nTurn {self.turn} concluded')
        print('____________________________________')

        self.turn = self.turn + 1

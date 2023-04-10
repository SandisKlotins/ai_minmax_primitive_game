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
        self.id: int = 0
        self.human_health: int = self.turns[0][0][self.human_player]['health']
        self.human_shields: int = self.turns[0][0][self.human_player]['shields']
        self.ai_health: int = self.turns[0][0][self.ai_player]['health']
        self.ai_shields: int = self.turns[0][0][self.ai_player]['shields']

    def processFirstTurn(self, spell: str) -> None:
        # Play out first turn
        # Set game to start on 1st turn (1st choice)
        self.turn = self.turn + 1

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
            self.id = best_option['id']

        else:
            # Process human turn
            option: dict = [node for node in options if node['spell'] == spell][0]
            self.human_health = option[self.human_player]['health']
            self.human_shields = option[self.human_player]['shields']
            self.ai_health = option[self.ai_player]['health']
            self.ai_shields = option[self.ai_player]['shields']
            self.id = option['id']

        print('____________________________________')
        print(f"Player {options[0]['player']} attacks with {spell}")
        print(f'Human health = {self.human_health}, shields = {self.human_shields}\nAI health = {self.ai_health}, shields = {self.ai_shields}\nTurn {self.turn} concluded')
        print('____________________________________')

        self.turn = self.turn + 1

    def processTurn(self, spell: str) -> None:
        # Play out regular turn

        if self.human_health > 0 and self.ai_health > 0:

            options: list[dict] = [option for option in self.turns[self.turn] if self.id in option['previous_id']]

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
                self.id = best_option['id']

            else:
                # Process human turn
                # option: dict = [node for node in options if node['spell'] == spell][0]
                option: list[dict] = options
                # Initial hope here was to simply get the correct option by spell name
                # But during dedup more than one noce can appear with the same
                # Must brute the option by calculating the turn product (logic oversight in initial development)
                op_1: dict = option[0]

                hp_diff: int = abs(op_1[self.ai_player]['health'] - self.ai_health)
                sh_diff: int = abs(op_1[self.ai_player]['shields'] - self.ai_shields)
                product: int = hp_diff + sh_diff
                print(f'product is {product}')
                # Each attack can produce a unique product, check which one is viable
                if spell == 'fire' and product == 10:
                    option = option[0]

                elif spell == 'fire':
                    option = option[1]

                if spell == 'frost' and (product == 15 or product == 5):
                    option = option[0]

                elif spell == 'frost':
                    option = option[1]

                self.human_health = option[self.human_player]['health']
                self.human_shields = option[self.human_player]['shields']
                self.ai_health = option[self.ai_player]['health']
                self.ai_shields = option[self.ai_player]['shields']
                self.id = option['id']

            print(f"Player {options[0]['player']} attacks with {spell}")
            print(f'Human health = {self.human_health}, shields = {self.human_shields}\nAI health = {self.ai_health}, shields = {self.ai_shields}\nTurn {self.turn} concluded')
            print('____________________________________')

            self.turn = self.turn + 1

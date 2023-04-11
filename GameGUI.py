import tkinter as tk
from tkinter import ttk
from Player import Player
from Game import Game
from TurnTree import TurnTree


class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Game")
        self.root.geometry("400x300")
        self.chosen_player = None
        self.chosen_first = None
        self.default_progress = 100

        self.game: Game
        self.turns: dict

        self.choose_player_label = tk.Label(root, text="Choose Player:")
        self.choose_player_label.pack()

        self.button_frame1 = tk.Frame(root)
        self.player1_button = tk.Button(self.button_frame1, text="Player 1", command=lambda: self.selectPlayer('p1'))
        self.player1_button.pack(side="left", padx=5)
        self.player2_button = tk.Button(self.button_frame1, text="Player 2", command=lambda: self.selectPlayer('p2'))
        self.player2_button.pack(side="left", padx=5)
        self.button_frame1.pack(pady=10)

        self.choose_first_label = tk.Label(root, text="Choose who goes first:", anchor="w")

        self.button_frame2 = tk.Frame(root)
        self.player1_first_button = tk.Button(self.button_frame2, text="Player 1", command=lambda: self.selectFirst('p1'))
        self.player1_first_button.pack(side="left", padx=5)
        self.player2_first_button = tk.Button(self.button_frame2, text="Player 2", command=lambda: self.selectFirst('p2'))
        self.player2_first_button.pack(side="left", padx=5)

        self.spell_label = tk.Label(root, text="Choose spell:", anchor="w")

        self.spell_frame = tk.Frame(root)
        self.fire_button = tk.Button(self.spell_frame, text="Fire", command=lambda: self.selectSpell("fire"))
        self.fire_button.pack(side="left", padx=5)
        self.frost_button = tk.Button(self.spell_frame, text="Frost", command=lambda: self.selectSpell("frost"))
        self.frost_button.pack(side="left", padx=5)

        self.retry_frame = tk.Frame(root)
        self.retry_button = tk.Button(self.retry_frame, text="Play again", command=lambda: self.reset())
        self.retry_button.pack(side="left", padx=5)

        self.progress_label_player_health = tk.Label(root, text="Placeholder", anchor="w")
        self.progress_bar_player_health = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        #self.progress_bar_player_health['value'] = self.default_progress

        self.progress_label_player_shields = tk.Label(root, text="Placeholder", anchor="w")
        self.progress_bar_player_shields = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        #self.progress_bar_player_shields['value'] = self.default_progress

        self.progress_label_ai_health = tk.Label(root, text="Placeholder", anchor="w")
        self.progress_bar_ai_health = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        #self.progress_bar_ai_health['value'] = self.default_progress

        self.progress_label_ai_shields = tk.Label(root, text="Placeholder", anchor="w")
        self.progress_bar_ai_shields = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        #self.progress_bar_ai_shields['value'] = self.default_progress

        self.hideProgressBar()

        self.is_ini: bool = False

    def selectPlayer(self, player) -> None:
        self.chosen_player = player
        self.button_frame1.pack_forget()
        self.choose_first_label.pack()
        self.button_frame2.pack(pady=10)

        self.choose_player_label.config(text=f'Choose Player: {self.chosen_player}')
        self.choose_first_label.pack()

    def selectFirst(self, first) -> None:
        self.chosen_first = first
        self.button_frame2.pack_forget()
        self.showProgressBar()

        self.choose_first_label.config(text=f'Choose who goes first: {self.chosen_first}')

        # All necessary params are now set
        # Initialize game, generate turns and evaluate them
        if self.is_ini == False:
            self.iniGame()
            self.is_ini = True

            self.progress_label_player_health.config(text=f'Remaining {self.game.human_player} health: {self.game.human_health}')
            self.progress_bar_player_health['value'] = self.game.human_health
            self.progress_label_player_shields.config(text=f'Remaining {self.game.human_player} shields: {self.game.human_shields}')
            self.progress_bar_player_shields['value'] = self.game.human_shields
            self.progress_label_ai_health.config(text=f'Remaining {self.game.ai_player} health: {self.game.ai_health}')
            self.progress_bar_ai_health['value'] = self.game.ai_health
            self.progress_label_ai_shields.config(text=f'Remaining {self.game.ai_player} shields: {self.game.ai_shields}')
            self.progress_bar_ai_shields['value'] = self.game.ai_shields


        self.spell_label.pack()
        self.spell_frame.pack()

    def iniGame(self) -> None:
        player_one = Player(ai=False if self.chosen_player == 'p1' else True)
        player_two = Player(ai=False if self.chosen_player == 'p2' else True)

        # Initialize and generate every possible turn with the above settings
        player_one_goes_first: bool = True if self.chosen_first == 'p1' else False
        turn_tree = TurnTree(
            player_one=player_one,
            player_two=player_two,
            player_one_goes_first=player_one_goes_first)

        # Generate every turn outcome
        turn_tree.generateTree()
        turn_tree.evaluateTree()
        self.turns = turn_tree.getTree()

        print(
            f'Initializing game\nPlayer one health = {player_one.getHealth()}, shields = {player_one.getShields()}\nPlayer two health = {player_two.getHealth()}, shields = {player_two.getShields()}')
        print(f'You are playing as {self.chosen_player}')

        # Initialize game with params
        self.game = Game(
            player=player_one, # doesnt matter which one, we just want the player class methods
            human_player=self.chosen_player,
            ai_player=turn_tree.ai_player,
            turns=self.turns,
            player_one_goes_first=player_one_goes_first)

    def selectSpell(self, spell: str) -> None:
        if self.game.turn == 0:
            self.game.processFirstTurn(spell) # Human turn
            self.game.processTurn(spell) # AI turn
            
        else:
            self.game.processTurn(spell) # Human turn
            self.game.processTurn(spell) # AI turn

        self.progress_label_player_health.config(text=f'Remaining {self.game.human_player} health: {self.game.human_health}')
        self.progress_bar_player_health['value'] = self.game.human_health
        self.progress_label_player_shields.config(text=f'Remaining {self.game.human_player} shields: {self.game.human_shields}')
        self.progress_bar_player_shields['value'] = self.game.human_shields
        self.progress_label_ai_health.config(text=f'Remaining {self.game.ai_player} health: {self.game.ai_health}')
        self.progress_bar_ai_health['value'] = self.game.ai_health
        self.progress_label_ai_shields.config(text=f'Remaining {self.game.ai_player} health: {self.game.ai_shields}')
        self.progress_bar_ai_shields['value'] = self.game.ai_shields

        if self.game.human_health <= 0 or self.game.ai_health <= 0:
            self.spell_frame.pack_forget()
            
            winner: str = self.game.human_player if self.game.human_health > 0 else self.game.ai_player
            self.spell_label.config(text=f'{winner} has won the game!\n Play again?')
            self.retry_frame.pack()
            print(f'{winner} has won the game!')

        self.root.update()

    def showProgressBar(self) -> None:
        self.progress_label_player_health.pack()
        self.progress_bar_player_health.pack()
        self.progress_label_player_shields.pack()
        self.progress_bar_player_shields.pack()

        self.progress_label_ai_health.pack()
        self.progress_bar_ai_health.pack()
        self.progress_label_ai_shields.pack()
        self.progress_bar_ai_shields.pack()


    def hideProgressBar(self) -> None:
        self.progress_label_player_health.pack_forget()
        self.progress_bar_player_health.pack_forget()
        self.progress_label_player_shields.pack_forget()
        self.progress_bar_player_shields.pack_forget()

        self.progress_label_ai_health.pack_forget()
        self.progress_bar_ai_health.pack_forget()
        self.progress_label_ai_shields.pack_forget()
        self.progress_bar_ai_shields.pack_forget()

    def reset(self) -> None:
        self.chosen_player = None
        self.chosen_first = None
        self.hideProgressBar()
        self.is_ini: bool = False
        self.retry_frame.pack_forget()
        self.spell_label.pack_forget()

        self.button_frame1.pack()
        self.button_frame2.pack()
        self.spell_label.config(text='Choose spell:')
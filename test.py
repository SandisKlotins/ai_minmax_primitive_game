import tkinter as tk
from Player import Player
from Game import Game
from TurnTree import TurnTree

class GameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Game")

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=20)

        self.label = tk.Label(self.button_frame, text="Choose player:")
        self.label.pack()

        # Add 10 pixels of padding around each button
        self.player1_button = tk.Button(self.button_frame, text="p1", command=lambda: self.select_player('p1'))
        self.player1_button.pack(pady=10)

        self.player2_button = tk.Button(self.button_frame, text="p2", command=lambda: self.select_player('p2'))
        self.player2_button.pack(pady=10)

        self.play_button = tk.Button(self.button_frame, text="Play the game", command=lambda: self.play_game())
        self.play_button.pack(pady=10)

        # Initialize attributes for chosen player and first turn player
        self.chosen_player: str = ''
        self.chosen_first: str = ''

    def select_player(self, player):
        self.chosen_player = player
        self.label.config(text=f"You chose Player {player}.")
        self.player1_button.destroy()
        self.player2_button.destroy()

        # Create a new frame to hold the second set of buttons
        self.button_frame2 = tk.Frame(self.master)
        self.button_frame2.pack(pady=20)

        self.label2 = tk.Label(self.button_frame2, text="Select who goes first:")
        self.label2.pack()

        # Add 10 pixels of padding around each button
        self.player1_first_button = tk.Button(self.button_frame2, text="p1", command=lambda: self.select_first(1))
        self.player1_first_button.pack(pady=10)

        self.player2_first_button = tk.Button(self.button_frame2, text="p2", command=lambda: self.select_first(2))
        self.player2_first_button.pack(pady=10)

    def select_first(self, first):
        self.chosen_first = first
        self.label2.config(text=f"{self.label2.cget('text')} You chose Player {first} to go first.")
        self.player1_first_button.destroy()
        self.player2_first_button.destroy()

        # Call your game code with self.chosen_player and self.chosen_first as inputs here

    def play_game(self):
        player_one = Player(ai=False if self.chosen_player == 'p1' else True)
        player_two = Player(ai=False if self.chosen_player == 'p2' else True)
        print(f'thingy is {self.chosen_player}')

        # Initialize and generate every possible turn with the above settings
        player_one_goes_first: bool = True if self.chosen_first == 'p1' else False
        turn_tree = TurnTree(
            player_one=player_one,
            player_two=player_two,
            player_one_goes_first=player_one_goes_first)

        # Generate every turn outcome
        turn_tree.generateTree()
        turn_tree.evaluateTree()
        turns: dict = turn_tree.getTree()

        print(
            f'Initializing game\nPlayer one health = {player_one.getHealth()}, shields = {player_one.getShields()}\nPlayer two health = {player_two.getHealth()}, shields = {player_two.getShields()}')
        print(f'You are playing as {self.chosen_player}')

        # Initialize game with params
        game = Game(player=player_one, # doesnt matter which one, we just want the player class methods
                    human_player=self.chosen_player,
                    ai_player=turn_tree.ai_player,
                    turns=turns,
                    player_one_goes_first=player_one_goes_first)

        # Play game
        game.processFirstTurn()
        while game.human_health > 0 and game.ai_health > 0:
            game.processTurn()

        if game.human_health > 0:
            print('Human player has won!')
        else:
            print('AI has won!')


root = tk.Tk()
my_game = GameGUI(root)
root.mainloop()
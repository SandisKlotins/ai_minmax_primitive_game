class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    def get_name(self):
        return self.name
        
    def update_score(self, points):
        self.score += points
        
class Game:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        
    def print_scores(self):
        print("Current scores:")
        print(f"{self.player_one.get_name()}: {self.player_one.score}")
        print(f"{self.player_two.get_name()}: {self.player_two.score}")


p1 = Player('David')
p2 = Player('Greg')
g = Game(p1, p2)
g.print_scores()
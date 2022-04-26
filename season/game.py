import random as r

class Game:

    team1 = ""
    team2 = ""
    
    # default constructor
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    # add functions for calculating winner
    def play_game(self):
        teams = [self.team1,self.team2]
        return r.choice(teams)
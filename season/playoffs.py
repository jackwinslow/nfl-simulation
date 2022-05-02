import random as r
from league import league
from league.team import Team
from league.division import Division
from season.game import Game

class Playoffs:

    # maybe break it down by playoff rounds 

    def __init__(self, teams):
        self.teams = teams

    def wild_card(self):
        loser_1 = Game(self.teams[1], self.teams[6]).play_playoff_game(False)
        loser_2 = Game(self.teams[3], self.teams[4]).play_playoff_game(False)
        loser_3 = Game(self.teams[2], self.teams[5]).play_playoff_game(False)
        self.teams.remove(loser_1)
        self.teams.remove(loser_2)
        self.teams.remove(loser_3)
    
    def divisional_round(self):
        loser_1 = Game(self.teams[0], self.teams[3]).play_playoff_game(False)
        loser_2 = Game(self.teams[1], self.teams[2]).play_playoff_game(False)
        self.teams.remove(loser_1)
        self.teams.remove(loser_2)
    
    def conference_round(self):
        loser = Game(self.teams[0], self.teams[1]).play_playoff_game(False)
        self.teams.remove(loser)

    # returns the winner of the conference    
    def get_conf_winner(self):
        self.wild_card()
        self.divisional_round()
        self.conference_round()
        return self.teams.pop()
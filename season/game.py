import random as r
from league import team

class Game:

    home = team.Team()
    away = team.Team()
    isDivG = False
    
    # default constructor
    def __init__(self, home, away):
        self.home = away
        self.home = away
        isDivG = self.home.get_division() == self.away.get_division()

    # add functions for calculating winner
    def play_game(self):
        # Step 1 Calculate prob of team1 beating team2
        home_WL = self.home.set_win_level()
        away_WL = self.away.set_win_level()
        """ I don't think there is an actual mathematical calculation to do here since they
            are not independent events, so although this is arbitrary it puts out a better
            compared to my last calculation output """
        P_home_W = (home_WL * (1 - away_WL)) / ((home_WL * (1 - away_WL)) + (away_WL * (1 - home_WL)))
        
        # Step 2 Play the game, boolean variable is true if team1 wins
        home_W = r.random() <= P_home_W
        
        # Step 3 edit records and outcomes
        if home_W:
            home_WL *= -1
            if isDivG: self.home.set_div_wins()
        else:
            away_WL *= -1
            if isDivG: self.away.set_div_wins()

        self.home.append_outcomes(away_WL)
        self.away.append_outcomes(home_WL)
        

        
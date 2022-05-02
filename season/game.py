import random as r
from league import team
from league.league import League

class Game:
    
    # default constructor
    def __init__(self, home, away):
        # self.nfl = 
        self.home = home
        self.away = away
        self.isDivG = self.home.get_division() == self.away.get_division()

    # add functions for calculating winner
    def play_game(self):
        # Step 1 Calculate prob of team1 beating team2
        self.home.set_win_level(True)
        self.away.set_win_level(False)
        home_WL = self.home.get_win_level()
        away_WL = self.away.get_win_level()
        """ I don't think there is an actual mathematical calculation to do here since they
            are not independent events, so although this is arbitrary it puts out a better
            compared to my last calculation output """
        P_home_W = (home_WL * (1 - away_WL)) / ((home_WL * (1 - away_WL)) + (away_WL * (1 - home_WL)))
        #P_home_W = home_WL / (home_WL + away_WL)
        # Step 2 Play the game, boolean variable is true if team1 wins
        rands = r.random()
        home_W = rands <= P_home_W
        
        # Step 3 edit records and outcomes
        if home_W:
            self.home.append_outcomes(away_WL)
            self.away.append_outcomes(-1 * home_WL)
            if self.isDivG: self.home.set_div_wins()
        else:
            self.home.append_outcomes(-1 * away_WL)
            self.away.append_outcomes(home_WL)
            if self.isDivG: self.away.set_div_wins()

        # print(f"{self.away.get_name()} ({(self.away.get_win_level())}) at {self.home.get_name()} ({(self.home.get_win_level())}) : {round(rands, 3)} <= {round(P_home_W, 3)} = {home_W}")

    def play_playoff_game(self, findWinner):
        # Step 1 Calculate prob of team1 beating team2
        self.home.set_win_level(True)
        self.away.set_win_level(False)
        home_WL = self.home.get_win_level()
        away_WL = self.away.get_win_level()
        """ I don't think there is an actual mathematical calculation to do here since they
            are not independent events, so although this is arbitrary it puts out a better
            compared to my last calculation output """
        P_home_W = (home_WL * (1 - away_WL)) / ((home_WL * (1 - away_WL)) + (away_WL * (1 - home_WL)))
        # P_home_W = home_WL / (home_WL + away_WL)
        # Step 2 Play the game, boolean variable is true if team1 wins
        home_W = r.random() <= P_home_W
        
        # Step 3 edit records and outcomes
        if home_W:
            self.home.append_outcomes(-1 * away_WL)
            self.away.append_outcomes(home_WL)
        else:
            self.home.append_outcomes(away_WL)
            self.away.append_outcomes(-1 * home_WL)

        # print(f"{self.away.get_name()} ({away_WL}) at {self.home.get_name()} ({home_WL}) : ")

        return [self.home, self.away][0 if findWinner else 1] if home_W else [self.away, self.home][0 if findWinner else 1]
        

        
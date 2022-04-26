import random as r
from league import Team

class Game:

    team1 = Team()
    team2 = Team()
    isDivG = False
    
    # default constructor
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        isDivG = self.team1.get_division() == self.team2.get_division()


    # add functions for calculating winner
    def play_game(self):
        # Step 1 Calculate prob of team1 beating team2
        t1_wp = self.team1.get_win_prob()
        t2_wp = self.team2.get_win_prob()
        p_t1_w = (t1_wp * (1 - t2_wp)) / ((t1_wp * (1 - t2_wp)) + (t2_wp * (1 - t1_wp)))
        
        # Step 2 Play the game, boolean variable is true if team1 wins
        is_t1_w = r.random() <= self.game_prob()
        
        # Step 3 edit records and outcomes
        self.team1.set_record(is_t1_w, self.isDivG)
        self.team2.set_record(not is_t1_w, self.isDivG)
        self.team1.append_outcomes(t2_wp if is_t1_w else -1 * t2_wp)
        self.team2.append_outcomes(-1 * t1_wp if is_t1_w else t1_wp)

        # Step 4 set win probs
        self.team1.set_win_prob()
        self.team2.set_win_prob()
        

        
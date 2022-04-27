import random as r
from league import team

class Game:

    team1 = team.Team()
    team2 = team.Team()
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
        """ I don't think there is an actual mathematical calculation to do here since they
            are not independent events, so although this is arbitrary it puts out a better
            compared to my last calculation output """
        p_t1_w = t1_wp / (t1_wp + t2_wp)
        
        # Step 2 Play the game, boolean variable is true if team1 wins
        is_t1_w = r.random() <= p_t1_w
        
        # Step 3 edit records and outcomes
        if is_t1_w:
            t1_wp *= -1
            if isDivG: self.team1.set_div_wins()
        else:
            t2_wp *= -1
            if isDivG: self.team2.set_div_wins()

        self.team1.append_outcomes(t2_wp)
        self.team2.append_outcomes(t1_wp)

        # Step 4 set win probs for next game
        """ might be smart to have a process for whether it's a playoff game
            as the team that's eliminated shouldn't calculate their win
            prob as it's irrelevant """
        self.team1.set_win_prob()
        self.team2.set_win_prob()
        

        
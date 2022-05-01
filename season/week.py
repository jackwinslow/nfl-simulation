import random as r
import league 
from league import team
from league import division

class Week:

    week_schedule = []

    """
    either div, conf, non-conf, rank, 17
    """
    week_type = ""
    num_for_type = ""
    
    game_pairs = []

    # default constructor, haven't made significant edits
    def __init__(self, week_type, num_for_type):
        self.game_pairs = []

    # DIV WEEK
    def __init__(self, week_type, num_for_type):
        for div in league.get_divs():
            game_pair_1 = [div[0], div[1]]
            game_pair_2 = [div[2], div[3]]
            game_pair_3 = [div[1], div[2]]
            game_pair_4 = [div[0], div[3]]
            game_pair_5 = [div[0], div[2]]
            game_pair_6 = [div[1], div[3]]
            if num_for_type == 0:
                self.game_pairs.append(game_pair_1, game_pair_2)
            elif num_for_type == 1:
                self.game_pairs.append(reversed(game_pair_1), reversed(game_pair_2))
            elif num_for_type == 2:
                self.game_pairs.append(game_pair_3, game_pair_4)
            elif num_for_type == 3:
                self.game_pairs.append(reversed(game_pair_3), reversed(game_pair_4))
            elif num_for_type == 4:
                self.game_pairs.append(game_pair_5, game_pair_6)
            elif num_for_type == 5:
                self.game_pairs.append(reversed(game_pair_5), reversed(game_pair_6))
                

    def execute_week(self):
        result = []
        for matchup in range(0, len(self.week_schedule)):
            result.append(self.week_schedule[matchup].play_game())

        return result
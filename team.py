import random as r

class Team:

    name = ""
    conference = ""
    division = ""

    division_rank = 0
    conference_rank = 0
    league_rank = 0

    schedule = []

    current_record = [0, 0]
    outcomes = []

    skill_level = 0.0
    i_skill_level = 0.0

    matchup_factor = 0.0

    injuries = []
    health_level = 0.0

    moral_level = 0.0

    homefield_advantage = 0.0
    capacity_filled = 0.0

    prev_szn_rank = 0
    salary_cap = 0

    improvement_level = 0.0

    def __init__(self, name, conference, division):
        self.name = name
        self.conference = conference
        self.division = division

    def set_division_rank(self, rank):
        self.division_rank = rank

    def set_conference_rank(self, rank):
        self.conference_rank = rank

    def set_league_rank(self, rank):
        self.league_rank = rank
    
    def set_prev_szn_rank(self, rank):
        self.prev_szn_rank = rank

    def set_capaity(self, new_capacity):
        self.capacity_filled = new_capacity

    def add_game(self, game):
        if self.schedule.count(game) == 0:
            self.schedule.append(game)

    def get_division(self):
        return self.division
    
    def get_win_prob(self): 
        return self.health_level + self.moral_level + self.skill_level
    
    def get_prev_szn_rank(self):
        return self.prev_szn_rank

    def get_skill_level(self):
        return self.skill_level
    
    def get_improvement(self):
        return self.improvement_level

    def get_i_skill_level(self):
        return self.i_skill_level
    
    def get_record(self):
        return self.current_record

    def get_homefield(self):
        return self.homefield_advantage

    def get_name(self):
        return self.name

    def get_matchup_factor(self):
        return self.matchup_factor

    def get_morale(self):
        return self.moral_level

    def get_record(self):
        return self.current_record

    def set_i_skill_level(self):
        prev_influence = 1.0 - (self.get_prev_szn_rank() / 100.0)
        return self.improvement_level + prev_influence

    def set_record(self):
        win_count = len([w for w in self.outcomes.get_skill_level() if w > 0])
        loss_count = len(self.outcomes) - win_count
        return [win_count, loss_count]

    def set_skill_level(self):
        change = sum([x for x in self.outcomes.get_skill_level()])
        WL_factor = (len(self.outcomes)/21) * change 
        self.skill_level = self.i_skill_level + WL_factor  

    def set_win_prob(self, opponent):
        win_prob = 0.5 * self.skill_level
        win_prob += 0.2 * (opponent.get_matchup_factor() + self.health_level)
        win_prob += 0.08 * self.moral_level
        win_prob += 0.02 * self.homefield_advantage
import random
import numpy as np

class Team:

    def __init__(self, name, conference, division):
        self.name = name
        self.conference = conference
        self.division = division

        self.division_rank = 0
        self.conference_rank = 0
        self.league_rank = 0

        self.schedule = []

        self.current_record = [0, 0]
        self.div_wins = 0
        # strength of schedule
        self.sos = 0.0
        
        self.outcomes = []
        self.skill_level = 0.0
        self.i_skill_level = 0.0
        self.win_level = 0.0

        self.injuries = []
        self.health_level = 0.0

        self.morale_level = 0.0

        self.homefield_advantage = 0.0
        self.capacity_filled = 0.0

        self.prev_division_rank = 0
        self.prev_szn_rank = 0
        self.salary_cap = 0

        self.improvement_level = 0.0
        self.draft_rank = 0

        self.last_change = 0

    """def __init__(self):
        self.name = None"""
    
    def append_outcomes(self, outcome):
        self.outcomes.append(outcome)

    def set_outcomes(self, outcomes):
        self.outcomes = outcomes

    def set_sos(self, sos):
        self.sos = sos

    def get_draft_rank(self):
        return self.draft_rank
    
    def set_draft_rank(self, rank):
        self.draft_rank = rank

    def set_i_skill_level(self):
        prev_influence = 1.0 - (self.get_prev_szn_rank() / 34.0)
        self.set_improvement_level()
        self.i_skill_level = (0.01) * self.improvement_level + prev_influence

    def set_health_level(self):
        health_level = self.get_health_level()
        arr = self.get_injuries()
        for j in arr:
            if j > 0:
                j -= 1
                if j == 0:
                    if j <= 21:
                        health_level += 10
                    elif 22 <= j <= 39:
                        health_level += 3
                    else:
                        health_level += 1
        num_injured = random.randint(0,3)
        while num_injured != 0:
            #more likely for a starter to get injured
            #can't get injured twice
            selector = random.randint(0,4)
            if selector < 3:
                inj = random.randint(0,21)
                if arr[inj] > 0:
                    continue
            else:
                inj = random.randint(22,52)
                if arr[inj] > 0:
                    continue
            num_injured -= 1
            #set number of weeks out, with lower weeks more likely
            weeks = random.randint(1,100)
            if weeks <= 60:
                weeks = random.randint(1,4)
            elif 61 <= weeks <= 91:
                weeks = random.randint(5,9)
            elif 92 <= weeks <= 97:
                weeks = random.randint(10,12)
            else:
                weeks = random.randint(13,18)
            inj[1] = weeks
            #reduce health level based on whether starter, backup, or other is injured
            if inj <= 21:
                health_level -= 10
            elif 22 <= inj <= 39:
                health_level -= 3
            else:
                health_level -= 1
        self.health_level = health_level
        self.injuries = arr


        
    def set_healthy(self):
        #run at beginning of season to set team to healthy
        arr = []
        for i in range(53):
            arr[i] = 0
        self.health_level = 100
        self.injuries = arr


    def set_homefield_advantage(self):
        name = self.get_name()
        homefield_adv = 0
        list = [['Cardinals', 62622/63400], ['Falcons', 67586/71000], ['Ravens', 70537/71008], 
                ['Bills', 67816/71608], ['Panthers', 71906/74867], ['Bears', 60833/61500], 
                ['Bengals', 60325/65515], ['Browns', 67431/67895], ['Cowboys', 93421/100000], 
                ['Broncos', 76236/76500], ['Lions', 51522/65000], ['Packers', 77991/81441], 
                ['Texans', 66811/71795], ['Colts', 62475/67000], ['Jaguars', 59968/67264], 
                ['Chiefs', 73227/76416], ['Raiders', 61185/65000], ['Chargers', 70240/71000], 
                ['Rams', 71598/72000], ['Dolphins', 64374/65326], ['Vikings', 66701/67000], 
                ['Patriots', 65878/65900], ['Saints', 64929/74295], ['Giants', 73882/80242], 
                ['Jets', 71676/82500], ['Eagles', 69796/70000], ['Steelers', 60488/68400], 
                ['Fourty_Niners', 66670/68500], ['Seahawks', 68408/68740], ['Buccaneers', 65372/65890], 
                ['Titans', 68566/69143], ['Commanders', 52751/82000]]
        list = sorted(list, key = lambda l:l[1])
        #will return ranking from 1 to 32 with higher number being stronger homefield advantage (Patriots having highest at 32)
        for i in range(32):
            if list[i][0] == name:
                self.homefield_advantage = i+1
                self.capacity_filled = list[i][1]
    
    def set_improvement_level(self):
        picking_order = 33 - self.prev_szn_rank
        # drafting factor
        a = random.randint(1,99)
        if (a >= 69): # the picks won't be bad, statistic that in all first round picks, 16.7% didn't play for that team, 32% were useless, 13.7% were poor players
            m = 1+(1/(-a+101)) # multiplier that changes exponentially the closer a gets to 100 (99 being an all star/ hall of famer) highest value = 2
        else: 
            m = 1+(-1/(a**0.5)) ## players picked will range from bad to absolutely useless. wasting picks on major busts will tank the improvement level heavily

        self.improvement_level = (m**3)*(( (0.031*self.prev_szn_rank)+(1-(self.draft_rank+1000/1032)) )/2)
    
    def set_last_change(self, week):
        self.last_change = week
    
    def get_outcomes(self):
        return self.outcomes
    
    def set_morale_level(self):
        if len(self.outcomes) == 0: return
        out_morale = self.get_morale_level()
        streak = len(self.outcomes) - self.last_change
        previous_game_factor = random.uniform(1.18,1.2+(streak*0.012))
        if (self.outcomes[-1] > 0):
            out_morale*=previous_game_factor # generates a multiplier >= ~1.18
        else:
            out_morale*=(1-(previous_game_factor-1)) # generates a multiplier <= ~0.89

        if (1 >= random.randint(0,2)): # random event simulation
            major_event_factor = np.random.normal(0,1.5,None)/10
            out_morale+=major_event_factor
        self.morale_level = np.clip(out_morale,0.01,1)

    def set_record(self):
        win_count = len([w for w in self.outcomes.get_skill_level() if w > 0])
        loss_count = len(self.outcomes) - win_count
        return [win_count, loss_count]

    def set_div_wins(self):
        self.div_wins += 1

    def get_morale_level(self):
        return self.morale_level

    def set_div_wins_zero(self):
        self.div_wins = 0

    def p_w(self, opp):
        return (self.win_level * (1 - opp)) / ((self.win_level * (1 - opp)) + (opp * (1 - self.win_level)))

    def set_skill_level(self):
        if len(self.outcomes) == 0: 
            self.skill_level = self.i_skill_level
            return
        change = (1 if self.outcomes[-1] > 0 else -1) * (self.p_w(abs(self.outcomes[-1])))
        change /= 21
        if self.skill_level > 0.5:
            self.skill_level += (1 - self.skill_level) * change
        else:
            self.skill_level += self.skill_level * change  

    def set_win_level(self, isHome):
        self.set_skill_level()
        self.set_health_level()
        self.set_homefield_advantage()
        self.set_morale_level()
        skill = 0.99 * self.skill_level
        home = 0.005 * self.homefield_advantage
        morale = 0.005 * self.morale_level
        # health_level = self.health_level
        self.win_level = skill + home + morale # + health

    def set_win_level_zero(self):
        self.win_level = 0.0

    def set_division_rank(self, rank):
        self.division_rank = rank

    def set_conference_rank(self, rank):
        self.conference_rank = rank

    def set_league_rank(self, rank):
        self.league_rank = rank
    
    def set_prev_division_rank(self, rank):
        self.prev_division_rank = rank

    def set_prev_szn_rank(self, rank):
        self.prev_szn_rank = rank

    def set_capacity(self, new_capacity):
        self.capacity_filled = new_capacity

    def get_outcomes(self):
        return self.outcomes

    def get_division(self):
        return self.division
    
    def get_win_level(self): 
        return self.win_level
    
    def get_prev_szn_rank(self):
        return self.prev_szn_rank
    
    def get_prev_div_rank(self):
        return self.prev_division_rank

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

    def get_morale(self):
        return self.morale_level

    def get_record(self):
        return self.current_record
    
    def get_div_wins(self):
        return self.div_wins

    def get_win_prob(self):
        return self.win_prob

    def get_health_level(self):
        return self.health_level

    def get_injuries(self):
        return self.injuries
    
    def get_wins(self):
        return len([x for x in self.outcomes if x > 0])

    def get_losses(self):
        return len([x for x in self.outcomes if x < 0])

    def get_sos(self):
        return np.sum(np.absolute(np.array(self.outcomes)))

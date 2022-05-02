import random as r
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
        
        self.super_bowls = 0

    """def __init__(self):
        self.name = None"""

    def set_super_bowls(self):
        self.super_bowls += 1
    
    def append_outcomes(self, outcome):
        self.outcomes.append(outcome)

    def set_outcomes(self, outcomes):
        self.outcomes = outcomes

    def set_sos(self, sos):
        self.sos = sos

    def set_i_skill_level(self):
        prev_influence = 1 - (self.get_prev_szn_rank() / 34.0)
        self.i_skill_level = self.improvement_level + prev_influence
        self.skill_level = self.i_skill_level

    def set_health_level(self):
        arr = self.get_injuries()
        health_level = self.get_health_level()
        for j in arr:
        if j[1] > 0:
            j[1] -= 1
            if j[1] == 0:
                if j[0] <= 21:
                    health_level += 10
                elif 22 <= j[0] <= 39:
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
                if arr[inj][1] == 0:
                    inj = arr[inj]
            else:
                inj = random.randint(22,52)
                if arr[inj][1] == 0:
                    inj = arr[inj]
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
            if inj[0] <= 21:
                health_level -= 10
            elif 22 <= inj[0] <= 39:
                health_level -= 3
            else:
                health_level -= 1
        self.health_level = health_level
        self.injuries = arr
    
    #run at start of season
    def set_healthy(self):
        rows, cols = (53, 2)
        arr = []
        for i in range(rows):
            col = []
            for j in range(cols):
                if j == 0:
                    col.append(i)
                else:
                    col.append(0)
            arr.append(col)
        self.health_level = 100
        self.injuries = arr

    def set_homefield_advantage(self):
        name = self.get_name()
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
    
    def set_morale_level(self,offseason,win,streak):
        out_morale = self.get_morale_level()
        if (offseason):
            win, streak = False, 0
            if (1 >= r.randint(0,4)):
                major_event_factor = np.random.normal(0,2,None)/10
                out_morale+=major_event_factor
            i = self.get_improvement_level()
            out_morale = out_morale*(1-i) +i
        
        else:
            previous_game_factor = r.uniform(1.18,1.2+(streak*0.012))
            if (win):
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

    def set_div_wins_zero(self):
        self.div_wins = 0

    def p_w(self, opp):
        s = self.win_level
        return (s * (1 - opp)) / ((s * (1 - opp)) + (s * (1 - opp)))

    def set_skill_level(self):
        if len(self.outcomes) == 0: return
        change = (1 if self.outcomes[-1] > 0 else -1) * (self.p_w(abs(self.outcomes[-1])))
        change /= 21
        if self.skill_level > 0.5:
            self.skill_level += (1 - self.skill_level) * change
        else:
            self.skill_level += self.skill_level * change

    def set_win_level(self, isHome):
        self.set_skill_level()
        self.set_health_level()
        self.set_morale_level()
        self.set_homefield_advantage()
        # self.win_level = (1 * self.skill_level) + 0 * self.health_level
        # self.win_level += 0 * self.morale_level
        # self.win_level += ((1 if isHome else 0) * 0 * self.homefield_advantage)
        self.win_level = self.skill_level

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

    def set_capaity(self, new_capacity):
        self.capacity_filled = new_capacity

    def get_super_bowls(self):
        return self.super_bowls

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
    
    def get_improvement_level(self):
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
<<<<<<< HEAD

    def get_SB(self):
        return self.super_bowls

    def reset_all(self):
        self.set_i_skill_level()
        self.division_rank = 0
        self.conference_rank = 0
        self.league_rank = 0
        self.schedule = []
        self.current_record = [0, 0]
        self.div_wins = 0
        self.sos = 0.0
        self.outcomes = []
        self.injuries = []
        self.health_level = 0.0
        self.morale_level = 0.0
        self.homefield_advantage = 0.0
        self.capacity_filled = 0.0
        self.improvement_level = 0.0

    def reset_SB(self):
        self.super_bowls = 0
=======
>>>>>>> cc918be7a1b11b638041bf42fbb9e2d8ac9661c0

import random as r
from league import league
from league.team import Team
from league.division import Division
from season.game import Game

class Week:

    # default constructor, haven't made significant edits
    def __init__(self, year, week_type, num_for_type):
        self.games = []
        self.week_type = week_type
        if week_type == "DIV": self.div_week(num_for_type)
        elif week_type == "CONF-DIV": self.conf_week(year, num_for_type)
        elif week_type == "NON-CONF-DIV": self.nonconf_week(year, num_for_type)
        elif week_type == "RANK": self.rank_week(year, num_for_type)
        else: self.random_week(year)

    def get_week_type(self):
        return self.week_type
        
    def div_week(self, num_for_type):
        for divis in league.get_divs():
            div = divis.get_teams()
            if num_for_type == 0:
                self.games.append(Game(div[0], div[1]))
                self.games.append(Game(div[2], div[3]))
            elif num_for_type == 1:
                self.games.append(Game(div[1], div[2]))
                self.games.append(Game(div[0], div[3]))
            elif num_for_type == 2:
                self.games.append(Game(div[0], div[2]))
                self.games.append(Game(div[1], div[3]))
            elif num_for_type == 3:
                self.games.append(Game(div[1], div[0]))
                self.games.append(Game(div[3], div[2]))
            elif num_for_type == 4:
                self.games.append(Game(div[2], div[1]))
                self.games.append(Game(div[0], div[3]))
            elif num_for_type == 5:
                self.games.append(Game(div[2], div[0]))
                self.games.append(Game(div[3], div[1]))

        # print('div week', len(self.games))

    def run_mats(self, year, num_for_type, mats):
        for mat in mats:
            if num_for_type == 0:
                for x in range(4):
                    self.games.append(Game(mat[0].get_team(x), mat[1].get_team(x)))
            elif num_for_type == 1:
                for x in range(4):
                    self.games.append(Game(mat[0].get_team(x), mat[1].get_team(3-x)))
            elif num_for_type == 2:
                self.games.append(Game(mat[1].get_team(0), mat[0].get_team(1)))
                self.games.append(Game(mat[1].get_team(1), mat[0].get_team(3)))
                self.games.append(Game(mat[1].get_team(2), mat[0].get_team(0)))
                self.games.append(Game(mat[1].get_team(3), mat[0].get_team(2)))
            elif num_for_type == 3:
                self.games.append(Game(mat[1].get_team(0), mat[0].get_team(2)))
                self.games.append(Game(mat[1].get_team(1), mat[0].get_team(0)))
                self.games.append(Game(mat[1].get_team(2), mat[0].get_team(3)))
                self.games.append(Game(mat[1].get_team(3), mat[0].get_team(1)))

    def conf_week(self, year, num_for_type):
        divs = league.get_divs()
        AFC = divs[:4]
        NFC = divs[4:]
        mats = [[AFC[0], AFC[1]], [AFC[2], AFC[3]], [NFC[0], NFC[1]], [NFC[2], NFC[3]]]
        if year == 1:
            mats = [[AFC[0], AFC[3]], [AFC[1], AFC[2]], [NFC[0], NFC[3]], [NFC[1], NFC[2]]]
        elif year == 2:
            mats = [[AFC[0], AFC[2]], [AFC[1], AFC[3]], [NFC[0], NFC[2]], [NFC[1], NFC[3]]]
        self.run_mats(year, num_for_type, mats)

        # print('conf week', len(self.games))

    def nonconf_week(self, year, num_for_type):
        divs = league.get_divs()
        AFC = divs[:4]
        NFC = divs[4:]
        mats = [[AFC[0], NFC[1]], [AFC[2], NFC[0]], [AFC[3], NFC[3]], [AFC[1], NFC[2]]]
        if year == 1:
            mats = [[AFC[0], NFC[2]], [AFC[2], NFC[1]], [AFC[3], NFC[0]], [AFC[1], NFC[3]]]
        elif year == 2:
            mats = [[AFC[0], NFC[3]], [AFC[2], NFC[2]], [AFC[3], NFC[1]], [AFC[1], NFC[0]]]
        self.run_mats(year, num_for_type, mats)

        # print('nonconf week', len(self.games))


    def rank_week(self, year, num_for_type):
        divs = league.get_divs()
        AFC = divs[:4]
        NFC = divs[4:]
        mats = [[AFC[0], AFC[1]], [AFC[2], AFC[3]], [NFC[0], NFC[1]], [NFC[2], NFC[3]]]
        if year == 1:
            mats = [[AFC[0], AFC[3]], [AFC[1], AFC[2]], [NFC[0], NFC[3]], [NFC[1], NFC[2]]]
        elif year == 2:
            mats = [[AFC[0], AFC[2]], [AFC[1], AFC[3]], [NFC[0], NFC[2]], [NFC[1], NFC[3]]]
        AFC_MATS = mats[:2]
        NFC_MATS = mats[2:]
        if num_for_type == 0:
            for t in AFC_MATS[0][0].get_teams():
                opp = AFC_MATS[1][0].get_team(t.get_prev_div_rank() - 1)
                self.games.append(Game(t, opp))
            for t in AFC_MATS[0][1].get_teams():
                opp = AFC_MATS[1][1].get_team(t.get_prev_div_rank() - 1)
                self.games.append(Game(t, opp))
            for t in NFC_MATS[0][0].get_teams():
                opp = NFC_MATS[1][0].get_team(t.get_prev_div_rank() - 1)
                self.games.append(Game(t, opp))
            for t in NFC_MATS[0][1].get_teams():
                opp = NFC_MATS[1][1].get_team(t.get_prev_div_rank() - 1)
                self.games.append(Game(t, opp))
        elif num_for_type == 1:
            for t in AFC_MATS[0][0].get_teams():
                opp = AFC_MATS[1][1].get_team(t.get_prev_div_rank() - 1)
                self.games.append(Game(t, opp))
            for t in AFC_MATS[0][1].get_teams():
                opp = AFC_MATS[1][0].get_team(t.get_prev_div_rank() - 1)
                self.games.append(Game(t, opp))
            for t in NFC_MATS[0][0].get_teams():
                opp = NFC_MATS[1][1].get_team(t.get_prev_div_rank() - 1)
                self.games.append(Game(t, opp))
            for t in NFC_MATS[0][1].get_teams():
                opp = NFC_MATS[1][0].get_team(t.get_prev_div_rank() - 1)
                self.games.append(Game(t, opp))

    def random_week(self, year):
        divs = league.get_divs()
        AFC = divs[:4]
        NFC = divs[4:]
        mats = [[AFC[0], NFC[3]], [AFC[1], NFC[0]], [AFC[2], NFC[1]], [AFC[3], NFC[2]]]
        if year == 1:
            mats = [[AFC[0], NFC[2]], [AFC[1], NFC[1]], [AFC[2], NFC[0]], [AFC[3], NFC[3]]]
        elif year == 2:
            mats = [[AFC[0], NFC[1]], [AFC[1], NFC[3]], [AFC[2], NFC[2]], [AFC[3], NFC[0]]]
        for mat in mats:
            cur_div = mat[0].get_teams()
            opp_1 = mat[1].get_team(cur_div[0].get_prev_div_rank() - 1)
            opp_2 = mat[1].get_team(cur_div[1].get_prev_div_rank() - 1)
            opp_3 = mat[1].get_team(cur_div[2].get_prev_div_rank() - 1)
            opp_4 = mat[1].get_team(cur_div[3].get_prev_div_rank() - 1)
            self.games.append(Game(cur_div[0], opp_1))
            self.games.append(Game(cur_div[1], opp_2))
            self.games.append(Game(cur_div[2], opp_3))
            self.games.append(Game(cur_div[3], opp_4))
            

    # print('rank week', len(self.games))

    def get_games(self):
        return self.games
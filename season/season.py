import random as r
import season

class Season:

    reg_season = season.regular_season.RegularSeason()
    playoffs = season.playoffs.Playoffs()

    def __init__(self, reg_season, playoffs):
        self.reg_season = reg_season
        self.playoffs = playoffs
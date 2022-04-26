import random as r

class RegularSeason:

    regular_season_schedule = []

    # default constructor
    def __init__(self, regular_season_schedule):
        self.regular_season_schedule = regular_season_schedule

    def execute_regular_season(self):
        result = []
        for week in range(0, len(self.regular_season_schedule)):
            result.append(self.regular_season_schedule[week].execute_week())

        return result
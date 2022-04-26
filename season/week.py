import random as r

class Week:

    week_schedule = []

    # default constructor
    def __init__(self, week_schedule):
        self.week_schedule = week_schedule

    def execute_week(self):
        result = []
        for matchup in range(0, len(self.week_schedule)):
            result.append(self.week_schedule[matchup].play_game())

        return result
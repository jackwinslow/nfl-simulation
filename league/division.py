from league.team import Team

class Division:

    """team_0 = Team()
    team_1 = Team()
    team_2 = Team()
    team_3 = Team()"""

    def __init__(self, team_0, team_1, team_2, team_3):
        self.team_0 = team_0
        self.team_1 = team_1
        self.team_2 = team_2
        self.team_3 = team_3

    """def __init__(self):
        self.name = None"""

    def get_team(self, team_num):
        return [self.team_0, self.team_1, self.team_2, self.team_3][team_num]

    def get_teams(self):
        return [self.team_0, self.team_1, self.team_2, self.team_3]

    # Design Divison Standings
    # - something interesting about this is that it is not as relevant to 
    #   a team's week to week play, so this is something that could perhaps
    #   be calculated only at the end of the season when organizing the playoffs
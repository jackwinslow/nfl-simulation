from league import team

class Division:

    team_1 = team.Team()
    team_2 = team.Team()
    team_3 = team.Team()
    team_4 = team.Team()

    def __init__(self, team_1, team_2, team_3, team_4):
        self.team_1 = team_1
        self.team_2 = team_2
        self.team_3 = team_3
        self.team_4 = team_4

    def get_teams(self):
        return [self.team_1, self.team_2, self.team_3, self.team_4]

    # Design Divison Standings
    # - something interesting about this is that it is not as relevant to 
    #   a team's week to week play, so this is something that could perhaps
    #   be calculated only at the end of the season when organizing the playoffs
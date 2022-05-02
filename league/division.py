from league.team import Team
from league.league import League

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

    def calc_and_set_rank():
        afc_east = []
        afc_north = []
        afc_south = []
        afc_west = []
        nfc_east = []
        nfc_north = []
        nfc_south = []
        nfc_west = []

        # AFC
        for team in League.AFC.East.get_teams():
            afc_east.append(team)

        for team in League.AFC.North.get_teams():
            afc_north.append(team)

        for team in League.AFC.South.get_teams():
            afc_south.append(team)

        for team in League.AFC.West.get_teams():
            afc_west.append(team)

        # NFC
        for team in League.NFC.East.get_teams():
            nfc_east.append(team)

        for team in League.NFC.North.get_teams():
            nfc_north.append(team)

        for team in League.NFC.South.get_teams():
            nfc_south.append(team)

        for team in League.NFC.West.get_teams():
            nfc_west.append(team)

        afc_east.sort(key=lambda x: (x.get_wins(), x.get_div_wins(), x.get_sos()), reverse=True)
        afc_north.sort(key=lambda x: (x.get_wins(), x.get_div_wins(), x.get_sos()), reverse=True)
        afc_south.sort(key=lambda x: (x.get_wins(), x.get_div_wins(), x.get_sos()), reverse=True)
        afc_west.sort(key=lambda x: (x.get_wins(), x.get_div_wins(), x.get_sos()), reverse=True)
        nfc_east.sort(key=lambda x: (x.get_wins(), x.get_div_wins(), x.get_sos()), reverse=True)
        nfc_north.sort(key=lambda x: (x.get_wins(), x.get_div_wins(), x.get_sos()), reverse=True)
        nfc_south.sort(key=lambda x: (x.get_wins(), x.get_div_wins(), x.get_sos()), reverse=True)
        nfc_west.sort(key=lambda x: (x.get_wins(), x.get_div_wins(), x.get_sos()), reverse=True)

        for x in range(len(afc_east)):
            afc_east[x].set_division_rank(x + 1)

        for x in range(len(afc_north)):
            afc_north[x].set_division_rank(x + 1)

        for x in range(len(afc_south)):
            afc_south[x].set_division_rank(x + 1)

        for x in range(len(afc_west)):
            afc_west[x].set_division_rank(x + 1)

        for x in range(len(nfc_east)):
            nfc_east[x].set_division_rank(x + 1)

        for x in range(len(nfc_north)):
            nfc_north[x].set_division_rank(x + 1)

        for x in range(len(nfc_south)):
            nfc_south[x].set_division_rank(x + 1)

        for x in range(len(nfc_west)):
            nfc_west[x].set_division_rank(x + 1)

        return afc_east, afc_north, afc_south, afc_west, nfc_east, nfc_north, nfc_south, nfc_west

    # Design Divison Standings
    # - something interesting about this is that it is not as relevant to 
    #   a team's week to week play, so this is something that could perhaps
    #   be calculated only at the end of the season when organizing the playoffs
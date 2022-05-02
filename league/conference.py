from league.division import Division
from league.league import League

class Conference:

    """North = Division()
    South = Division()
    East = Division()
    West = Division()"""

    def __init__(self, East, North, South, West):
        self.North = North
        self.South = South
        self.East = East
        self.West = West

    def calc_and_set_rank():
        afc = []
        nfc = []

        # AFC
        for team in League.AFC.East.get_teams():
            afc.append(team)

        for team in League.AFC.North.get_teams():
            afc.append(team)

        for team in League.AFC.South.get_teams():
            afc.append(team)

        for team in League.AFC.West.get_teams():
            afc.append(team)

        # NFC
        for team in League.NFC.East.get_teams():
            nfc.append(team)

        for team in League.NFC.North.get_teams():
            nfc.append(team)

        for team in League.NFC.South.get_teams():
            nfc.append(team)

        for team in League.NFC.West.get_teams():
            nfc.append(team)

        afc.sort(key=lambda x: (x.get_wins(), x.get_sos()), reverse=True)
        nfc.sort(key=lambda x: (x.get_wins(), x.get_sos()), reverse=True)

        for x in range(len(afc)):
            afc[x].set_conference_rank(x + 1)

        for x in range(len(nfc)):
            nfc[x].set_conference_rank(x + 1)

        return afc, nfc

    # Design Conference Standings
    # - This along with Division standings is likely only important for the playoff
    #   schedule 
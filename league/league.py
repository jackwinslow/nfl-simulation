from league.team import Team
from league.division import Division
from league.conference import Conference

class League:

    # American Football Conference

    Bills = Team("Bills", "AFC", "East")
    Bills.set_prev_szn_rank(8)
    Bills.set_prev_division_rank(1)

    Patriots = Team("Patriots", "AFC", "East")
    Patriots.set_prev_szn_rank(12)
    Patriots.set_prev_division_rank(2)

    Dolphins = Team("Dolphins", "AFC", "East")
    Dolphins.set_prev_szn_rank(18)
    Dolphins.set_prev_division_rank(3)

    Jets = Team("Jets", "AFC", "East")
    Jets.set_prev_szn_rank(29)
    Jets.set_prev_division_rank(4)

    AFC_EAST = Division(Bills, Patriots, Dolphins, Jets)

    Bengals = Team("Bengals", "AFC", "North")
    Bengals.set_prev_szn_rank(2)
    Bengals.set_prev_division_rank(1)

    Steelers = Team("Steelers", "AFC", "North")
    Steelers.set_prev_szn_rank(13)
    Steelers.set_prev_division_rank(2)

    Browns = Team("Browns", "AFC", "North")
    Browns.set_prev_szn_rank(20)
    Browns.set_prev_division_rank(3)

    Ravens = Team("Ravens", "AFC", "North")
    Ravens.set_prev_szn_rank(19)
    Ravens.set_prev_division_rank(4)

    AFC_NORTH = Division(Bengals, Steelers, Browns, Ravens)

    Titans = Team("Titans", "AFC", "South")
    Titans.set_prev_szn_rank(7)
    Titans.set_prev_division_rank(1)

    Colts = Team("Colts", "AFC", "South")
    Colts.set_prev_szn_rank(17)
    Colts.set_prev_division_rank(2)

    Texans = Team("Texans", "AFC", "South")
    Texans.set_prev_szn_rank(30)
    Texans.set_prev_division_rank(3)

    Jaguars = Team("Jaguars", "AFC", "South")
    Jaguars.set_prev_szn_rank(32)
    Jaguars.set_prev_division_rank(4)

    AFC_SOUTH = Division(Titans, Colts, Texans, Jaguars)

    Chiefs = Team("Chiefs", "AFC", "West")
    Chiefs.set_prev_szn_rank(3)
    Chiefs.set_prev_division_rank(1)

    Raiders = Team("Raiders", "AFC", "West")
    Raiders.set_prev_szn_rank(11)
    Raiders.set_prev_division_rank(2)

    Chargers = Team("Chargers", "AFC", "West")
    Chargers.set_prev_szn_rank(16)
    Chargers.set_prev_division_rank(3)

    Broncos = Team("Broncos", "AFC", "West")
    Broncos.set_prev_szn_rank(24)
    Broncos.set_prev_division_rank(4)

    AFC_WEST = Division(Chiefs, Raiders, Chargers, Broncos)

    # National Football Conference 

    Cowboys = Team("Cowboys", "NFC", "East")
    Cowboys.set_prev_szn_rank(9)
    Cowboys.set_prev_division_rank(1)

    Eagles = Team("Eagles", "NFC", "East")
    Eagles.set_prev_szn_rank(14)
    Eagles.set_prev_division_rank(2)

    Commanders = Team("Commanders", "NFC", "East")
    Commanders.set_prev_szn_rank(22)
    Commanders.set_prev_division_rank(3)

    Giants = Team("Giants", "NFC", "East")
    Giants.set_prev_szn_rank(28)
    Giants.set_prev_division_rank(4)

    NFC_EAST = Division(Cowboys, Eagles, Commanders, Giants)

    Packers = Team("Packers", "NFC", "North")
    Packers.set_prev_szn_rank(5)
    Packers.set_prev_division_rank(1)

    Vikings = Team("Vikings", "NFC", "North")
    Vikings.set_prev_szn_rank(21)
    Vikings.set_prev_division_rank(2)

    Bears = Team("Bears", "NFC", "North")
    Bears.set_prev_szn_rank(26)
    Bears.set_prev_division_rank(3)

    Lions = Team("Lions", "NFC", "North")
    Lions.set_prev_szn_rank(31)
    Lions.set_prev_division_rank(4)

    NFC_NORTH = Division(Packers, Vikings, Bears, Lions)

    Buccaneers = Team("Buccaneers", "NFC", "South")
    Buccaneers.set_prev_szn_rank(6)
    Buccaneers.set_prev_division_rank(1)

    Saints = Team("Saints", "NFC", "South")
    Saints.set_prev_szn_rank(15)
    Saints.set_prev_division_rank(2)

    Falcons = Team("Falcons", "NFC", "South")
    Falcons.set_prev_szn_rank(25)
    Falcons.set_prev_division_rank(3)

    Panthers = Team("Panthers", "NFC", "South")
    Panthers.set_prev_szn_rank(27)
    Panthers.set_prev_division_rank(4)

    NFC_SOUTH = Division(Buccaneers, Saints, Falcons, Panthers)

    Rams = Team("Rams", "NFC", "West")
    Rams.set_prev_szn_rank(1)
    Rams.set_prev_division_rank(1)

    Cardinals = Team("Cardinals", "NFC", "West")
    Cardinals.set_prev_szn_rank(10)
    Cardinals.set_prev_division_rank(2)

    Fourty_Niners = Team("Fourty_Niners", "NFC", "West")
    Fourty_Niners.set_prev_szn_rank(4)
    Fourty_Niners.set_prev_division_rank(3)

    Seahawks = Team("Seahawks", "NFC", "West")
    Seahawks.set_prev_szn_rank(23)
    Seahawks.set_prev_division_rank(4)

    NFC_WEST = Division(Rams, Cardinals, Fourty_Niners, Seahawks)

    AFC = Conference(AFC_EAST, AFC_NORTH, AFC_SOUTH, AFC_WEST)
    NFC = Conference(NFC_EAST, NFC_NORTH, NFC_SOUTH, NFC_WEST)  

    def __init__(self):
        self.AFC = Conference(self.AFC_EAST, self.AFC_NORTH, self.AFC_SOUTH, self.AFC_WEST)
        self.NFC = Conference(self.NFC_EAST, self.NFC_NORTH, self.NFC_SOUTH, self.NFC_WEST)  

    def get_divs(self):
        return [self.AFC_EAST, self.AFC_NORTH, self.AFC_SOUTH, self.AFC_WEST, self.NFC_EAST, self.NFC_NORTH, self.NFC_SOUTH, self.NFC_WEST]
        
    def super_reset(self):
        for div in self.get_divs():
            for team in div.get_teams():
                team.reset_SB()

    def get_div(self, div):
        if div == "AFC EAST": return self.AFC_EAST
        elif div == "AFC WEST": return self.AFC_WEST 
        elif div == "AFC NORTH": return self.AFC_NORTH 
        elif div == "AFC SOUTH": return self.AFC_SOUTH 
        elif div == "NFC EAST": return self.NFC_EAST
        elif div == "NFC WEST": return self.NFC_WEST 
        elif div == "NFC NORTH": return self.NFC_NORTH 
        elif div == "NFC SOUTH": return self.NFC_SOUTH 
        else: return None

    def SB_counts(self):
        data = {}
        for team in self.AFC.East.get_teams():
            data.update({f"{team.get_name()}": [0,0,0]})
        for team in self.AFC.North.get_teams():
            data.update({f"{team.get_name()}": [0,0,0]})
        for team in self.AFC.South.get_teams():
            data.update({f"{team.get_name()}": [0,0,0]})
        for team in self.AFC.West.get_teams():
            data.update({f"{team.get_name()}": [0,0,0]})
        for team in self.NFC.East.get_teams():
            data.update({f"{team.get_name()}": [0,0,0]})
        for team in self.NFC.North.get_teams():
            data.update({f"{team.get_name()}": [0,0,0]})
        for team in self.NFC.South.get_teams():
            data.update({f"{team.get_name()}": [0,0,0]})
        for team in self.NFC.West.get_teams():
            data.update({f"{team.get_name()}": [0,0,0]})
        return data
        
    def reset_data(self):

        # AFC
        for team in self.AFC.East.get_teams():
            prev_div_rank = team.division_rank
            prev_League_rank = team.league_rank
            name = team.get_name()
            conference = team.get_conference()
            division = team.get_division()
            team = Team(name, conference, division)

        for team in self.AFC.North.get_teams():
            prev_div_rank = team.division_rank
            prev_League_rank = team.league_rank
            name = team.get_name()
            conference = team.get_conference()
            division = team.get_division()
            team = Team(name, conference, division)

        for team in self.AFC.South.get_teams():
            prev_div_rank = team.division_rank
            prev_League_rank = team.league_rank
            name = team.get_name()
            conference = team.get_conference()
            division = team.get_division()
            team = Team(name, conference, division)

        for team in self.AFC.West.get_teams():
            prev_div_rank = team.division_rank
            prev_League_rank = team.league_rank
            name = team.get_name()
            conference = team.get_conference()
            division = team.get_division()
            team = Team(name, conference, division)

        # NFC
        for team in self.NFC.East.get_teams():
            prev_div_rank = team.division_rank
            prev_League_rank = team.league_rank
            name = team.get_name()
            conference = team.get_conference()
            division = team.get_division()
            team = Team(name, conference, division)

        for team in self.NFC.North.get_teams():
            prev_div_rank = team.division_rank
            prev_League_rank = team.league_rank
            name = team.get_name()
            conference = team.get_conference()
            division = team.get_division()
            team = Team(name, conference, division)

        for team in self.NFC.South.get_teams():
            prev_div_rank = team.division_rank
            prev_League_rank = team.league_rank
            name = team.get_name()
            conference = team.get_conference()
            division = team.get_division()
            team = Team(name, conference, division)

        for team in self.NFC.West.get_teams():
            prev_div_rank = team.division_rank
            prev_League_rank = team.league_rank
            name = team.get_name()
            conference = team.get_conference()
            division = team.get_division()
            team = Team(name, conference, division)

        #print('Reset Team Season Data')

    def set_league_rank(self):
        league = []

        # AFC
        for team in self.AFC.East.get_teams():
            league.append(team)

        for team in self.AFC.North.get_teams():
            league.append(team)

        for team in self.AFC.South.get_teams():
            league.append(team)

        for team in self.AFC.West.get_teams():
            league.append(team)

        # NFC
        for team in self.NFC.East.get_teams():
            league.append(team)

        for team in self.NFC.North.get_teams():
            league.append(team)

        for team in self.NFC.South.get_teams():
            league.append(team)

        for team in self.NFC.West.get_teams():
            league.append(team)

        league.sort(key=lambda x: (x.get_wins(), x.get_sos()), reverse=True)

        for x in range(len(league)):
            league[x].set_league_rank(x + 1)

        return league

    def set_conference_rank(self):
        afc = []
        nfc = []

        # AFC
        for team in self.AFC.East.get_teams():
            afc.append(team)

        for team in self.AFC.North.get_teams():
            afc.append(team)

        for team in self.AFC.South.get_teams():
            afc.append(team)

        for team in self.AFC.West.get_teams():
            afc.append(team)

        # NFC
        for team in self.NFC.East.get_teams():
            nfc.append(team)

        for team in self.NFC.North.get_teams():
            nfc.append(team)

        for team in self.NFC.South.get_teams():
            nfc.append(team)

        for team in self.NFC.West.get_teams():
            nfc.append(team)

        afc.sort(key=lambda x: (x.get_wins(), x.get_sos()), reverse=True)
        nfc.sort(key=lambda x: (x.get_wins(), x.get_sos()), reverse=True)

        for x in range(len(afc)):
            afc[x].set_conference_rank(x + 1)

        for x in range(len(nfc)):
            nfc[x].set_conference_rank(x + 1)

        return afc, nfc
        
    def set_div_rank(self):
        afc_east = []
        afc_north = []
        afc_south = []
        afc_west = []
        nfc_east = []
        nfc_north = []
        nfc_south = []
        nfc_west = []

        # AFC
        for team in self.AFC.East.get_teams():
            afc_east.append(team)

        for team in self.AFC.North.get_teams():
            afc_north.append(team)

        for team in self.AFC.South.get_teams():
            afc_south.append(team)

        for team in self.AFC.West.get_teams():
            afc_west.append(team)

        # NFC
        for team in self.NFC.East.get_teams():
            nfc_east.append(team)

        for team in self.NFC.North.get_teams():
            nfc_north.append(team)

        for team in self.NFC.South.get_teams():
            nfc_south.append(team)

        for team in self.NFC.West.get_teams():
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


    def calc_playoff_seeds(self):
        afc = []
        nfc = []

        afc_rankings, nfc_rankings = self.set_conference_rank()
        afc_east, afc_north, afc_south, afc_west, nfc_east, nfc_north, nfc_south, nfc_west = self.set_div_rank()

        # AFC
        afc.append(afc_east[0]); afc_rankings.remove(afc_east[0])
        afc.append(afc_north[0]); afc_rankings.remove(afc_north[0])
        afc.append(afc_south[0]); afc_rankings.remove(afc_south[0])
        afc.append(afc_west[0]); afc_rankings.remove(afc_west[0])
        afc.sort(key=lambda x: (x.get_wins(), x.get_sos()), reverse=True)
        afc.append(afc_rankings[0])
        afc.append(afc_rankings[1])
        afc.append(afc_rankings[2])

        # NFC
        nfc.append(nfc_east[0]); nfc_rankings.remove(nfc_east[0])
        nfc.append(nfc_north[0]); nfc_rankings.remove(nfc_north[0])
        nfc.append(nfc_south[0]); nfc_rankings.remove(nfc_south[0])
        nfc.append(nfc_west[0]); nfc_rankings.remove(nfc_west[0])
        nfc.sort(key=lambda x: (x.get_wins(), x.get_sos()), reverse=True)
        nfc.append(nfc_rankings[0])
        nfc.append(nfc_rankings[1])
        nfc.append(nfc_rankings[2])

        return afc, nfc



    # League Standings
    # - This is really only important for the NFL Draft
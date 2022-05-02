from league.team import Team
from league.division import Division
from league.conference import Conference

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

def get_divs():
    return [AFC_EAST, AFC_NORTH, AFC_SOUTH, AFC_WEST, NFC_EAST, NFC_NORTH, NFC_SOUTH, NFC_WEST]

class League:

    AFC = Conference(AFC_EAST, AFC_NORTH, AFC_SOUTH, AFC_WEST)
    NFC = Conference(NFC_EAST, NFC_NORTH, NFC_SOUTH, NFC_WEST)  

    def __init__(self):
        self = self

    def get_div(self, div):
        if div == "AFC EAST": return AFC_EAST
        elif div == "AFC WEST": return AFC_WEST 
        elif div == "AFC NORTH": return AFC_NORTH 
        elif div == "AFC SOUTH": return AFC_SOUTH 
        elif div == "NFC EAST": return NFC_EAST
        elif div == "NFC WEST": return NFC_WEST 
        elif div == "NFC NORTH": return NFC_NORTH 
        elif div == "NFC SOUTH": return NFC_SOUTH 
        else: return None

    def reset_data():

        # AFC
        for team in League.AFC.East.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []

        for team in League.AFC.North.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []

        for team in League.AFC.South.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []

        for team in League.AFC.West.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []

        # NFC
        for team in League.NFC.East.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []

        for team in League.NFC.North.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []

        for team in League.NFC.South.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []

        for team in League.NFC.West.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []

        print('Reset Team Season Data')
        

    # League Standings
    # - This is really only important for the NFL Draft
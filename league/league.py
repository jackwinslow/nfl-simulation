from league.team import Team
from league.division import Division
from league.conference import Conference

# American Football Conference

Bills = Team("Bills", "AFC", "East")
Bills.set_prev_szn_rank(8)
Bills.set_prev_division_rank(1)
Bills.set_i_skill_level()

Patriots = Team("Patriots", "AFC", "East")
Patriots.set_prev_szn_rank(12)
Patriots.set_prev_division_rank(2)
Patriots.set_i_skill_level()

Dolphins = Team("Dolphins", "AFC", "East")
Dolphins.set_prev_szn_rank(18)
Dolphins.set_prev_division_rank(3)
Dolphins.set_i_skill_level()

Jets = Team("Jets", "AFC", "East")
Jets.set_prev_szn_rank(29)
Jets.set_prev_division_rank(4)
Jets.set_i_skill_level()

AFC_EAST = Division(Bills, Patriots, Dolphins, Jets)

Bengals = Team("Bengals", "AFC", "North")
Bengals.set_prev_szn_rank(2)
Bengals.set_prev_division_rank(1)
Bengals.set_i_skill_level()

Steelers = Team("Steelers", "AFC", "North")
Steelers.set_prev_szn_rank(13)
Steelers.set_prev_division_rank(2)
Steelers.set_i_skill_level()

Browns = Team("Browns", "AFC", "North")
Browns.set_prev_szn_rank(20)
Browns.set_prev_division_rank(3)
Browns.set_i_skill_level()

Ravens = Team("Ravens", "AFC", "North")
Ravens.set_prev_szn_rank(19)
Ravens.set_prev_division_rank(4)
Ravens.set_i_skill_level()

AFC_NORTH = Division(Bengals, Steelers, Browns, Ravens)

Titans = Team("Titans", "AFC", "South")
Titans.set_prev_szn_rank(7)
Titans.set_prev_division_rank(1)
Titans.set_i_skill_level()

Colts = Team("Colts", "AFC", "South")
Colts.set_prev_szn_rank(17)
Colts.set_prev_division_rank(2)
Colts.set_i_skill_level()

Texans = Team("Texans", "AFC", "South")
Texans.set_prev_szn_rank(30)
Texans.set_prev_division_rank(3)
Texans.set_i_skill_level()

Jaguars = Team("Jaguars", "AFC", "South")
Jaguars.set_prev_szn_rank(32)
Jaguars.set_prev_division_rank(4)
Jaguars.set_i_skill_level()

AFC_SOUTH = Division(Titans, Colts, Texans, Jaguars)

Chiefs = Team("Chiefs", "AFC", "West")
Chiefs.set_prev_szn_rank(3)
Chiefs.set_prev_division_rank(1)
Chiefs.set_i_skill_level()

Raiders = Team("Raiders", "AFC", "West")
Raiders.set_prev_szn_rank(11)
Raiders.set_prev_division_rank(2)
Raiders.set_i_skill_level()

Chargers = Team("Chargers", "AFC", "West")
Chargers.set_prev_szn_rank(16)
Chargers.set_prev_division_rank(3)
Chargers.set_i_skill_level()

Broncos = Team("Broncos", "AFC", "West")
Broncos.set_prev_szn_rank(24)
Broncos.set_prev_division_rank(4)
Broncos.set_i_skill_level()

AFC_WEST = Division(Chiefs, Raiders, Chargers, Broncos)

# National Football Conference 

Cowboys = Team("Cowboys", "NFC", "East")
Cowboys.set_prev_szn_rank(9)
Cowboys.set_prev_division_rank(1)
Cowboys.set_i_skill_level()

Eagles = Team("Eagles", "NFC", "East")
Eagles.set_prev_szn_rank(14)
Eagles.set_prev_division_rank(2)
Eagles.set_i_skill_level()

Commanders = Team("Commanders", "NFC", "East")
Commanders.set_prev_szn_rank(22)
Commanders.set_prev_division_rank(3)
Commanders.set_i_skill_level()

Giants = Team("Giants", "NFC", "East")
Giants.set_prev_szn_rank(28)
Giants.set_prev_division_rank(4)
Giants.set_i_skill_level()

NFC_EAST = Division(Cowboys, Eagles, Commanders, Giants)

Packers = Team("Packers", "NFC", "North")
Packers.set_prev_szn_rank(5)
Packers.set_prev_division_rank(1)
Packers.set_i_skill_level()

Vikings = Team("Vikings", "NFC", "North")
Vikings.set_prev_szn_rank(21)
Vikings.set_prev_division_rank(2)
Vikings.set_i_skill_level()

Bears = Team("Bears", "NFC", "North")
Bears.set_prev_szn_rank(26)
Bears.set_prev_division_rank(3)
Bears.set_i_skill_level()

Lions = Team("Lions", "NFC", "North")
Lions.set_prev_szn_rank(31)
Lions.set_prev_division_rank(4)
Lions.set_i_skill_level()

NFC_NORTH = Division(Packers, Vikings, Bears, Lions)

Buccaneers = Team("Buccaneers", "NFC", "South")
Buccaneers.set_prev_szn_rank(6)
Buccaneers.set_prev_division_rank(1)
Buccaneers.set_i_skill_level()

Saints = Team("Saints", "NFC", "South")
Saints.set_prev_szn_rank(15)
Saints.set_prev_division_rank(2)
Saints.set_i_skill_level()

Falcons = Team("Falcons", "NFC", "South")
Falcons.set_prev_szn_rank(25)
Falcons.set_prev_division_rank(3)
Falcons.set_i_skill_level()

Panthers = Team("Panthers", "NFC", "South")
Panthers.set_prev_szn_rank(27)
Panthers.set_prev_division_rank(4)
Panthers.set_i_skill_level()

NFC_SOUTH = Division(Buccaneers, Saints, Falcons, Panthers)

Rams = Team("Rams", "NFC", "West")
Rams.set_prev_szn_rank(1)
Rams.set_prev_division_rank(1)
Rams.set_i_skill_level()

Cardinals = Team("Cardinals", "NFC", "West")
Cardinals.set_prev_szn_rank(10)
Cardinals.set_prev_division_rank(2)
Cardinals.set_i_skill_level()

Fourty_Niners = Team("Fourty_Niners", "NFC", "West")
Fourty_Niners.set_prev_szn_rank(4)
Fourty_Niners.set_prev_division_rank(3)
Fourty_Niners.set_i_skill_level()

Seahawks = Team("Seahawks", "NFC", "West")
Seahawks.set_prev_szn_rank(23)
Seahawks.set_prev_division_rank(4)
Seahawks.set_i_skill_level()

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
            team.set_i_skill_level()

        for team in League.AFC.North.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []
            team.set_i_skill_level()

        for team in League.AFC.South.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []
            team.set_i_skill_level()

        for team in League.AFC.West.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []
            team.set_i_skill_level()

        # NFC
        for team in League.NFC.East.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []
            team.set_i_skill_level()

        for team in League.NFC.North.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []
            team.set_i_skill_level()

        for team in League.NFC.South.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []
            team.set_i_skill_level()

        for team in League.NFC.West.get_teams():
            team.prev_division_rank = team.division_rank
            team.prev_szn_rank = team.league_rank
            team.division_rank = 0
            team.conference_rank = 0
            team.league_rank = 0
            team.div_wins = 0
            team.outcomes = []
            team.set_i_skill_level()

        print('Reset Team Season Data')

    def calc_and_set_rank():
        league = []

        # AFC
        for team in League.AFC.East.get_teams():
            league.append(team)

        for team in League.AFC.North.get_teams():
            league.append(team)

        for team in League.AFC.South.get_teams():
            league.append(team)

        for team in League.AFC.West.get_teams():
            league.append(team)

        # NFC
        for team in League.NFC.East.get_teams():
            league.append(team)

        for team in League.NFC.North.get_teams():
            league.append(team)

        for team in League.NFC.South.get_teams():
            league.append(team)

        for team in League.NFC.West.get_teams():
            league.append(team)

        league.sort(key=lambda x: (x.get_wins(), x.get_sos()), reverse=True)

        for x in range(len(league)):
            league[x].set_league_rank(x + 1)

        return league
        

    # League Standings
    # - This is really only important for the NFL Draft
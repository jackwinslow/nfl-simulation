from league.team import Team
from league.division import Division
from league.conference import Conference

# American Football Conference

Patriots = Team("Patriots", "AFC", "East")
Patriots.set_prev_szn_rank(12)

Jets = Team("Jets", "AFC", "East")
Jets.set_prev_szn_rank(29)

Dolphins = Team("Dolphins", "AFC", "East")
Dolphins.set_prev_szn_rank(18)

Bills = Team("Bills", "AFC", "East")
Bills.set_prev_szn_rank(8)

AFC_EAST = Division(Patriots, Jets, Dolphins, Bills)

Bengals = Team("Bengals", "AFC", "North")
Bengals.set_prev_szn_rank(2)

Steelers = Team("Steelers", "AFC", "North")
Steelers.set_prev_szn_rank(13)

Browns = Team("Browns", "AFC", "North")
Browns.set_prev_szn_rank(20)

Ravens = Team("Ravens", "AFC", "North")
Ravens.set_prev_szn_rank(19)

AFC_NORTH = Division(Bengals, Steelers, Browns, Ravens)

Titans = Team("Titans", "AFC", "South")
Titans.set_prev_szn_rank(7)

Colts = Team("Colts", "AFC", "South")
Colts.set_prev_szn_rank(17)

Texans = Team("Texans", "AFC", "South")
Texans.set_prev_szn_rank(30)

Jaguars = Team("Jaguars", "AFC", "South")
Jaguars.set_prev_szn_rank(32)

AFC_SOUTH = Division(Titans, Colts, Texans, Jaguars)

Chiefs = Team("Chiefs", "AFC", "West")
Chiefs.set_prev_szn_rank(3)

Raiders = Team("Raiders", "AFC", "West")
Raiders.set_prev_szn_rank(11)

Chargers = Team("Chargers", "AFC", "West")
Chargers.set_prev_szn_rank(16)

Broncos = Team("Broncos", "AFC", "West")
Broncos.set_prev_szn_rank(24)

AFC_WEST = Division(Chiefs, Raiders, Chargers, Broncos)

# National Football Conference 

Cowboys = Team("Cowboys", "NFC", "East")
Cowboys.set_prev_szn_rank(9)

Eagles = Team("Eagles", "NFC", "East")
Eagles.set_prev_szn_rank(14)

Commanders = Team("Commanders", "NFC", "East")
Commanders.set_prev_szn_rank(22)

Giants = Team("Giants", "NFC", "East")
Giants.set_prev_szn_rank(28)

NFC_EAST = Division(Cowboys, Eagles, Commanders, Giants)

Packers = Team("Packers", "NFC", "North")
Packers.set_prev_szn_rank(5)

Vikings = Team("Vikings", "NFC", "North")
Vikings.set_prev_szn_rank(21)

Bears = Team("Bears", "NFC", "North")
Bears.set_prev_szn_rank(26)

Lions = Team("Lions", "NFC", "North")
Lions.set_prev_szn_rank(31)

NFC_NORTH = Division(Packers, Vikings, Bears, Lions)

Buccaneers = Team("Buccaneers", "NFC", "South")
Buccaneers.set_prev_szn_rank(6)

Saints = Team("Saints", "NFC", "South")
Saints.set_prev_szn_rank(15)

Falcons = Team("Falcons", "NFC", "South")
Falcons.set_prev_szn_rank(25)

Panthers = Team("Panthers", "NFC", "South")
Panthers.set_prev_szn_rank(27)

NFC_SOUTH = Division(Buccaneers, Saints, Falcons, Panthers)

Rams = Team("Rams", "NFC", "West")
Rams.set_prev_szn_rank(1)

Cardinals = Team("Cardinals", "NFC", "West")
Cardinals.set_prev_szn_rank(10)

Fourty_Niners = Team("Fourty_Niners", "NFC", "West")
Fourty_Niners.set_prev_szn_rank(4)

Seahawks = Team("Seahawks", "NFC", "West")
Fourty_Niners.set_prev_szn_rank(23)

NFC_WEST = Division(Rams, Cardinals, Fourty_Niners, Seahawks)

def get_divs():
    return [AFC_EAST, AFC_NORTH, AFC_SOUTH, AFC_WEST, NFC_EAST, NFC_NORTH, NFC_SOUTH, NFC_WEST]

class League:

    def __init__(self):
        AFC = Conference(self.AFC_EAST, self.AFC_NORTH, self.AFC_SOUTH, self.AFC_WEST)
        NFC = Conference(self.NFC_EAST, self.NFC_NORTH, self.NFC_SOUTH, self.NFC_WEST)  

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


        

    # League Standings
    # - This is really only important for the NFL Draft
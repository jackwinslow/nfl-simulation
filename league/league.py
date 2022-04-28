import league

class League:

    year_num = 0

    # American Football Conference

    Patriots = league.team.Team("Patriots", "AFC", "East")
    Patriots.set_prev_szn_rank(12)

    Jets = league.team.Team("Jets", "AFC", "East")
    Jets.set_prev_szn_rank(29)

    Dolphins = league.team.Team("Dolphins", "AFC", "East")
    Dolphins.set_prev_szn_rank(18)

    Bills = league.team.Team("Bills", "AFC", "East")
    Bills.set_prev_szn_rank(8)

    AFC_EAST = league.division.Division(Patriots, Jets, Dolphins, Bills)

    Bengals = league.team.Team("Bengals", "AFC", "North")
    Bengals.set_prev_szn_rank(2)
    
    Steelers = league.team.Team("Steelers", "AFC", "North")
    Steelers.set_prev_szn_rank(13)
    
    Browns = league.team.Team("Browns", "AFC", "North")
    Browns.set_prev_szn_rank(20)
    
    Ravens = league.team.Team("Ravens", "AFC", "North")
    Ravens.set_prev_szn_rank(19)

    AFC_NORTH = league.division.Division(Bengals, Steelers, Browns, Ravens)

    Titans = league.team.Team("Titans", "AFC", "South")
    Titans.set_prev_szn_rank(7)

    Colts = league.team.Team("Colts", "AFC", "South")
    Colts.set_prev_szn_rank(17)

    Texans = league.team.Team("Texans", "AFC", "South")
    Texans.set_prev_szn_rank(30)

    Jaguars = league.team.Team("Jaguars", "AFC", "South")
    Jaguars.set_prev_szn_rank(32)

    AFC_SOUTH = league.division.Division(Titans, Colts, Texans, Jaguars)

    Chiefs = league.team.Team("Chiefs", "AFC", "West")
    Chiefs.set_prev_szn_rank(3)

    Raiders = league.team.Team("Raiders", "AFC", "West")
    Raiders.set_prev_szn_rank(11)

    Chargers = league.team.Team("Chargers", "AFC", "West")
    Chargers.set_prev_szn_rank(16)

    Broncos = league.team.Team("Broncos", "AFC", "West")
    Broncos.set_prev_szn_rank(24)

    AFC_WEST = league.division.Division(Chiefs, Raiders, Chargers, Broncos)
    
    # National Football Conference 

    Cowboys = league.team.Team("Cowboys", "NFC", "East")
    Cowboys.set_prev_szn_rank(9)

    Eagles = league.team.Team("Eagles", "NFC", "East")
    Eagles.set_prev_szn_rank(14)

    Commanders = league.team.Team("Commanders", "NFC", "East")
    Commanders.set_prev_szn_rank(22)

    Giants = league.team.Team("Giants", "NFC", "East")
    Giants.set_prev_szn_rank(28)

    NFC_EAST = league.division.Division(Cowboys, Eagles, Commanders, Giants)

    Packers = league.team.Team("Packers", "NFC", "North")
    Packers.set_prev_szn_rank(5)

    Vikings = league.team.Team("Vikings", "NFC", "North")
    Vikings.set_prev_szn_rank(21)

    Bears = league.team.Team("Bears", "NFC", "North")
    Bears.set_prev_szn_rank(26)

    Lions = league.team.Team("Lions", "NFC", "North")
    Lions.set_prev_szn_rank(31)

    NFC_NORTH = league.division.Division(Packers, Vikings, Bears, Lions)

    Buccaneers = league.team.Team("Buccaneers", "NFC", "South")
    Buccaneers.set_prev_szn_rank(6)

    Saints = league.team.Team("Saints", "NFC", "South")
    Saints.set_prev_szn_rank(15)

    Falcons = league.team.Team("Falcons", "NFC", "South")
    Falcons.set_prev_szn_rank(25)

    Panthers = league.team.Team("Panthers", "NFC", "South")
    Panthers.set_prev_szn_rank(27)

    NFC_SOUTH = league.division.Division(Buccaneers, Saints, Falcons, Panthers)

    Rams = league.team.Team("Rams", "NFC", "West")
    Rams.set_prev_szn_rank(1)
    
    Cardinals = league.team.Team("Cardinals", "NFC", "West")
    Cardinals.set_prev_szn_rank(10)
    
    Fourty_Niners = league.team.Team("Fourty_Niners", "NFC", "West")
    Fourty_Niners.set_prev_szn_rank(4)
    
    Seahawks = league.team.Team("Seahawks", "NFC", "West")
    Fourty_Niners.set_prev_szn_rank(23)

    NFC_WEST = league.division.Division(Rams, Cardinals, Fourty_Niners, Seahawks)

    def __init__(self):
        NFC = league.conference.Conference(self.NFC_NORTH, self.NFC_SOUTH, self.NFC_EAST, self.NFC_WEST) 
        AFC = league.conference.Conference(self.AFC_NORTH, self.AFC_SOUTH, self.AFC_EAST, self.AFC_WEST) 

    """def set_schedule(self, Team):
        week_nums = []
        for x in range(18): week_nums.append(x+1)
        division = Team.get_division()
        division_opponents = division.get_teams()
        division_opponents.remove(Team)
        for x in division_opponents:
            Team.add_game([x, "HOME"])
            Team.add_game([x, "AWAY"])
            x.add_game([Team, "AWAY"])
            x.add_game([Team, "HOME"])
        non_conf_div_opp = self.AFC_EAST
        conf_div_opp = self.AFC_EAST

        if division == self.AFC_EAST:
            non_conf_div_opp = self.NFC_NORTH
            conf_div_opp = self.AFC_NORTH"""


    """ 
    
    Div - 6
    in-conf Div - 4
    out-conf Div - 4

    3
    
    WEEK: Div
    1 - 2
    
    """
        
        
        

    # League Standings
    # - This is really only important for the NFL Draft
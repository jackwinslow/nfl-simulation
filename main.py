import random as r 
import league
from season.regular_season import RegularSeason
from season.week import Week
from season.game import Game

NFL = league.League()

schedule = []

"""def main():
    rs = RegularSeason([Week([Game("Patriots","Jets"),Game("Bills","Giants"),Game("Dolphins","Rams")]),
                        Week([Game("Dolphins","Jets"),Game("Patriots","Giants"),Game("Bills","Rams")]),
                        Week([Game("Dolphins","Giants"),Game("Patriots","Rams"),Game("Bills","Jets")])])

    return rs.execute_regular_season()
"""

def main():
    for x in range(6): schedule.append(Week("DIV", x))
    for x in range(4): schedule.append(Week("CONF-DIV", x))
    for x in range(4): schedule.append(Week("NON-CONF-DIV", x))
    for x in range(2): schedule.append(Week("RANK", x))
    schedule.append(Week("RIVAL", x))

print(main())
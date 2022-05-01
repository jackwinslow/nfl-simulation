import random as r 
from season.week import Week
from season.game import Game

"""def main():
    rs = RegularSeason([Week([Game("Patriots","Jets"),Game("Bills","Giants"),Game("Dolphins","Rams")]),
                        Week([Game("Dolphins","Jets"),Game("Patriots","Giants"),Game("Bills","Rams")]),
                        Week([Game("Dolphins","Giants"),Game("Patriots","Rams"),Game("Bills","Jets")])])

    return rs.execute_regular_season()
"""

def make_schedule(season):
    schedule = []
    for x in range(6): 
        schedule.append(Week(season, "DIV", x))
    for x in range(4): 
        schedule.append(Week(season, "CONF-DIV", x))
    for x in range(4): 
        schedule.append(Week(season, "NON-CONF-DIV", x))
    for x in range(2): 
        schedule.append(Week(season, "RANK", x))
    # schedule.append(Week(season, "RIVAL", x))
    return schedule

def main():
    season = 0
    while season < 3:
        schedule = make_schedule(season)
        print("HERE")
        trial_num = 0
        for wk in schedule:
            print('week')
            for game in wk.get_games():
                game.play_game()
        
        season += 1


main()
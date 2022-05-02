import random as r 
from season.week import Week
from season.game import Game
from league.league import League

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
    schedule.append(Week(season, "RANDOM", x))
    return schedule

def main():
    season = 0
    while season < 1:
        schedule = make_schedule(season)
        wk_count = 0
        for wk in schedule:
            print('==================', wk.get_week_type(), 'Week', wk_count, "========= Season", season)
            for game in wk.get_games():
                game.play_game()
            wk_count += 1

        # AFC
        for team in League.AFC.East.get_teams():
            print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

        for team in League.AFC.North.get_teams():
            print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

        for team in League.AFC.South.get_teams():
            print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

        for team in League.AFC.West.get_teams():
            print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

        # NFC
        for team in League.NFC.East.get_teams():
            print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

        for team in League.NFC.North.get_teams():
            print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

        for team in League.NFC.South.get_teams():
            print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

        for team in League.NFC.West.get_teams():
            print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

        league_rankings = League.calc_and_set_rank()
        for x in range(len(league_rankings)):
            num = str(x + 1) + '.'
            print(num,'\t',league_rankings[x].get_name())
        League.reset_data()
        season += 1


main()
import random as r 
from league import league
from season.week import Week
from season.game import Game
from season.playoffs import Playoffs
from league.league import League
from importlib import reload
import time as t

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

trials = 100

def main():
    outs = []
    for trial in range(trials):
        cur = []
        for season in range(3):
            wk_count = 0
            for wk in make_schedule(season):
                # print('==================', wk.get_week_type(), 'Week', wk_count, "========= Season", season)
                for game in wk.get_games():
                    game.play_game()
                wk_count += 1

            # # AFC
            # for team in League.AFC.East.get_teams():
            #     print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

            # for team in League.AFC.North.get_teams():
            #     print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

            # for team in League.AFC.South.get_teams():
            #     print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

            # for team in League.AFC.West.get_teams():
            #     print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

            # # NFC
            # for team in League.NFC.East.get_teams():
            #     print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

            # for team in League.NFC.North.get_teams():
            #     print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

            # for team in League.NFC.South.get_teams():
            #     print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

            # for team in League.NFC.West.get_teams():
            #     print(team.get_name(), ' - [', team.get_wins(), ',', team.get_losses(), ']', team.get_sos())

            league_rankings = League.set_league_rank()
            """for x in range(len(league_rankings)):
                num = str(x + 1) + '.'
                print(num,'\t',league_rankings[x].get_name())"""

            # afc_rankings, nfc_rankings = League.set_conference_rank()

            # afc_east, afc_north, afc_south, afc_west, nfc_east, nfc_north, nfc_south, nfc_west = League.set_div_rank()

            afc_playoffs, nfc_playoffs = League.calc_playoff_seeds()

            """print('\nAFC')
            for x in range(len(afc_playoffs)):
                num = str(x + 1) + '.'
                print(num,'\t',afc_playoffs[x].get_name())

            print('\nNFC')
            for x in range(len(nfc_playoffs)):
                num = str(x + 1) + '.'
                print(num,'\t',nfc_playoffs[x].get_name())"""

            AFC_champ = Playoffs(afc_playoffs).get_conf_winner()
            NFC_champ = Playoffs(nfc_playoffs).get_conf_winner()
            SB_champ = Game(AFC_champ, NFC_champ).play_playoff_game(True)
            
            # print(SB_champ.get_name())
            cur.append(SB_champ.get_name())
            League.reset_data()
        outs.append(cur)
        reload(league)
    print(outs)

start = t.time()
main()
end = t.time()

print()
print((end-start)/60)
print()
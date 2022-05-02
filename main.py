import random as r 
from league import league
from season.week import Week
from season.game import Game
from season.playoffs import Playoffs
from league.league import League

NFL = League()

def make_schedule(season):
    schedule = []
    for x in range(6): 
        schedule.append(Week(NFL, season, "DIV", x))
    for x in range(4): 
        schedule.append(Week(NFL, season, "CONF-DIV", x))
    for x in range(4): 
        schedule.append(Week(NFL, season, "NON-CONF-DIV", x))
    for x in range(2): 
        schedule.append(Week(NFL, season, "RANK", x))
    schedule.append(Week(NFL, season, "RANDOM", x))
    return schedule

trials = 100

def main():
    for trial in range(trials):
        for season in range(3):
            schedule = make_schedule(season)
            wk_count = 0
            for wk in schedule:
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

            """league_rankings = NFL.set_league_rank()
            for x in range(len(league_rankings)):
                num = str(x + 1) + '.'
                print(num,'\t',league_rankings[x].get_name())"""

            # afc_rankings, nfc_rankings = League.set_conference_rank()

            # afc_east, afc_north, afc_south, afc_west, nfc_east, nfc_north, nfc_south, nfc_west = League.set_div_rank()

            afc_playoffs, nfc_playoffs = NFL.calc_playoff_seeds()

            """print('\nAFC')
            for x in range(len(afc_playoffs)):
                num = str(x + 1) + '.'
                print(num,'\t',afc_playoffs[x].get_name())

            print('\nNFC')
            for x in range(len(nfc_playoffs)):
                num = str(x + 1) + '.'
                print(num,'\t',nfc_playoffs[x].get_name())"""

            AFC_Conf_champ = Playoffs(afc_playoffs).get_conf_winner()
            NFC_Conf_champ = Playoffs(nfc_playoffs).get_conf_winner()
            SB_champ = Game(AFC_Conf_champ, NFC_Conf_champ).play_playoff_game(True)
            SB_champ.set_super_bowls()
            NFL.reset_data()
        for team in NFL.get_teams():
            team.adjust(team.get_SB())
        NFL.super_reset()
        print(trial)
        
        


start = t.time()
main()
end = t.time()

for team in NFL.get_teams():
    team.SB_Data()

print(f"\n\n\n{end-start}\n\n\n")
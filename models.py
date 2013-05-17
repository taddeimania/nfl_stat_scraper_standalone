import os

class Player(object):


    def __str__(self):
        """ Player representation that will be written to file. (formatted)
            (stdout for now)
        """
        formatted_output = "{}\n{} {}\n".format(self.stat_dict['player'], self.season, self.team)
        del self.stat_dict['player']
        for stat_category, stat_value in self.stat_dict.items():
            formatted_output += "{}: {}\n".format(stat_category, stat_value)
        return formatted_output

    def __init__(self, stat_dict, season, team):
        self.stat_dict = stat_dict
        self.season = season
        self.team = team

    def persist(self, path):
        player_file = os.path.join(path, "{}.txt".format(self.stat_dict['player'].replace(', ', ',')))
        print player_file
        with open(player_file, 'w') as f:
            f.write(str(self))



stat_attr_map = {
    'Player': 'player',
    'Kicking_50+': 'fifty_plus',
    'Receiving_TD': 'reception_touchdowns',
    'Rushing_Yds Lost': 'yards_lost',
    'Punting_In 10': 'punt_in_ten',
    'Passing_Att': 'pass_attempts',
    'Passing_Pct': 'pass_percentage',
    'Rushing_Fm Lost': 'fumbles_lost',
    'G': 'games',
    'Kicking_XP-Att': 'extra_points',
    'Punting_Long': 'punt_long',
    'Defense_Stf': 'def_stuff',
    'Passing_Yards': 'pass_yards',
    'Kicking_1-29': 'one_to_twenty_nine',
    'Receiving_Target': 'reception_targets',
    'Rushing_TD': 'rush_touchdowns',
    'Kicking_30_39': 'thirty_to_thirty_nine',
    'Returns_Yards': 'kickoff_return_yards',
    'Defense_Int Yds': 'interception_yards',
    'Defense_FF': 'forced_fumble',
    'Kicking_40_49': 'forty_to_fourty_nine',
    'Punting_Net': 'punt_returned_net',
    'Passing_1st': 'pass_first_downs',
    'Passing_Int': 'pass_interceptions',
    'Rushing_Fmbl': 'fumbles',
    'Passing_TD': 'pass_touchdowns',
    'Rushing_Avg': 'average_rush',
    'Punting_Ret': 'punts_returned',
    'Passing_Rate': 'pass_rating',
    'Returns_KOR': 'kickoff_returns',
    'Defense_Int': 'interception',
    'Kicking_FG-Att': 'field_goals',
    'Kicking_Long': 'field_goal_long',
    'Receiving_Long': 'long_reception',
    'Punting_Yards': 'punts_returned_yards',
    'Returns_FC': 'punt_return_fair_catches',
    'Punting_In 20': 'punt_in_twenty',
    'Receiving_1st': 'reception_first_downs',
    'Defense_FR': 'fumble_recover',
    'Rushing_1st': 'rush_first_downs',
    'Passing_Comp': 'pass_completions',
    'Rushing_Long': 'long_rush',
    'GS': 'games_started',
    'Defense_PD': 'pass_defended',
    'Returns_Punt_Avg': 'punt_return_average',
    'Returns_PR': 'punt_returns',
    'Passing_Yards/Att': 'pass_yards_per_attempt',
    'Kicking_FG Pct': 'field_goal_percentage',
    'Receiving_Yards': 'reception_yards',
    'Punting_Punts': 'punts',
    'Returns_TD': 'kickoff_return_touchdowns',
    'Returns_Punt_TD': 'punt_return_touchdowns',
    'Returns_Avg': 'kickoff_return_average',
    'Rushing_Rush': 'rushes',
    'Defense_TD': 'defensive_touchdowns',
    'Rushing_Stuff': 'stuff',
    'Kicking_Avg Miss': 'average_miss',
    'Passing_Sacked': 'pass_sacked',
    'Receiving_Avg': 'average_reception',
    'Receiving_YAC': 'reception_yards_after_catch',
    'Rushing_Yards': 'rush_yards',
    'Returns_Long': 'kickoff_return_long',
    'Returns_Punt_Long': 'punt_return_long',
    'Defense_Sck': 'sacks',
    'Kicking_Points': 'points',
    'Punting_Avg': 'punt_average',
    'Punting_TB': 'punt_touchbacks',
    'Punting_FC': 'punt_fair_catches',
    'Punting_Blkd': 'punt_blocks',
    'Receiving_Rec': 'receptions',
    'Defense_Tk': 'tackles',
    'Punting_TD': 'punts_returned_touchdowns',
    'Returns_Punt_Yards': 'punt_return_yards',
    'Kicking_Avg Att': 'average_attempt',
    'Defense_Ast': 'tackles_assist'
}

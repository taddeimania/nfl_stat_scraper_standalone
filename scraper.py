from models import stat_attr_map, Player
import os

class StatScraper(object):

    def __init__(self, site, team, season, page):
        self.base_site = site
        self.site = site('tr')
        self.team = team
        self.season = season
        self.page = page.replace('.html', '')
        self.stat_categories = [u'Player']
        self.players = []
        self.parse_site()

    def parse_site(self):
        self.get_stat_categories()
        self.set_stats()

    def get_stat_categories(self):
        # scrapes header for page because many categories have same stat name
        # used to prepend stat category
        stat_grouping = self.base_site.find('h2').string

        categories = self.site[0].find_all('a')
        for category in categories:
            self.stat_categories.append(category.text)

        # our above hack doesn't fix punt/kick returns values so we are more specific
        # with this hack.
        if stat_grouping == "Returns":
            self.stat_categories[7] = 'Punt_Yards'
            self.stat_categories[8] = 'Punt_Avg'
            self.stat_categories[9] = 'Punt_Long'

        for i in range(1, len(self.site) - 1):
            # PROBABLY want to get position?  Shrug?
            player = {}
            for i, line in enumerate(filter(lambda a: a != '\n', self.site[i])):
                # go ahead and ignore player names, games played, and games started
                if self.stat_categories[i] not in ['Player', 'G', 'GS']:
                    search_string = "{}_{}".format(stat_grouping, self.stat_categories[i])
                else:
                    search_string = self.stat_categories[i]

                # another creepy hack thanks to player names coming in funky
                player[search_string] = line.string.replace(u'\xa0', u' ')
            self.players.append(player)


    def set_stats(self):
        # idea:  make a directory structure of seasons / teams / players.txt
        current_dir = os.path.dirname(os.path.abspath(__file__))
        team_season_dir = os.path.join(current_dir, self.season, self.team, self.page[:self.page.index('_')])
        os.makedirs(team_season_dir)
        for record in self.players:
            stat_dict = {}
            for record_key in record.keys():
                stat_dict[stat_attr_map[record_key]] = record[record_key]

            current_player = Player(stat_dict, self.season, self.team)
            current_player.persist(team_season_dir)
        #     print current_player

from config import pages, seasons, teams
from bs4 import BeautifulSoup
from scraper import StatScraper
import urllib2


def main():
    for team in teams:
        for page in pages:
            for year in seasons:
                url = "http://sportsillustrated.cnn.com/football/nfl/teams/stats/{}/{}/{}".format(year, team, page)
                site_to_scrape = BeautifulSoup(urllib2.urlopen(url))
            StatScraper(site_to_scrape, team, year, page)

print "Pulling down 2008-2012 team stats."

main()

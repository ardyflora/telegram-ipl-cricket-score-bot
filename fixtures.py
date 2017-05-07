import sqlite3
from datetime import datetime
import lxml.html
from dateutil import parser
from dateutil import tz

HERE = tz.tzlocal()

conn = sqlite3.connect('iplPoints.db')
c = conn.cursor()

series_url = 'http://www.espncricinfo.com/indian-premier-league-2017/content/series/1078425.html?template=fixtures'

gameFullSchedule = []


def conversion(teamName):
    conversion = {}
    conversion['Sunrisers Hyderabad'] = 'SRH'
    conversion['Royal Challengers Bangalore'] = 'RCB'
    conversion['Rising Pune Supergiant'] = 'RPS'
    conversion['Mumbai Indians'] = 'MI'
    conversion['Gujarat Lions'] = 'GL'
    conversion['Kolkata Knight Riders'] = 'KKR'
    conversion['Kings XI Punjab'] = 'KXIP'
    conversion['Delhi Daredevils'] = 'DD'
    conversion['TBC'] = 'TBC'
    return conversion[teamName]


def convertTeamNameIntoShortName(fixture):
    teamNames = fixture.split(' v ')
    firstTeamName = conversion(teamNames[0].strip())
    secondTeamName = conversion(teamNames[1].strip())
    return firstTeamName + " v " + secondTeamName


tree = lxml.html.parse(series_url)
dates = tree.xpath(
    "//li[@class='large-20 medium-20 columns']/div[1]/span/text()")

gamesPlayedSofar = tree.xpath(
    "//li[@class='large-20 medium-20 columns']/div[2]/span/a/text()")
gameFullSchedule = gameFullSchedule + gamesPlayedSofar

gamesNotPlayedYet = tree.xpath(
    "//li[@class='large-20 medium-20 columns']/div[2]/span[1]/text()")
gameFullSchedule = gameFullSchedule + \
    list(filter(None, [x.rstrip() for x in gamesNotPlayedYet]))


countGame = 0

for i in range(0, len(dates)):
    if (i % 2 == 0):
        date_string = dates[i].strip() + ' ' + \
            dates[i + 1].split(u'\xa0')[0] + '+0530 2017'
        dt = parser.parse(date_string)
        c.execute("insert into fixtures (game,deadline) values (?,?)", [
                  convertTeamNameIntoShortName(gameFullSchedule[countGame].split('-')[1]), dt.astimezone(HERE)])
        countGame = countGame + 1

conn.commit()
conn.close()

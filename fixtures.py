import sqlite3
from datetime import datetime
import lxml.html
from dateutil import parser
from dateutil import tz

HERE = tz.tzlocal()

conn = sqlite3.connect('iplPoints.db')
c = conn.cursor()



class Fixtures:
	def __init__(self, url, gameScheduleList):
		self.url = url
		self.gameScheduleList = gameScheduleList

	def getFullSchedule(self):
		tree = lxml.html.parse(self.url)
		gamesPlayedSofar = tree.xpath(
		    "//li[@class='large-20 medium-20 columns']/div[2]/span/a/text()")
		self.gameScheduleList = self.gameScheduleList + gamesPlayedSofar

		gamesNotPlayedYet = tree.xpath(
		    "//li[@class='large-20 medium-20 columns']/div[2]/span[1]/text()")
		self.gameScheduleList = self.gameScheduleList + \
		    list(filter(None, [x.rstrip() for x in gamesNotPlayedYet]))

	def conversion(self,teamName):
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

	def convertTeamNameIntoShortName(self,fixture):
	    teamNames = fixture.split(' v ')
	    firstTeamName = self.conversion(teamNames[0].strip())
	    secondTeamName = self.conversion(teamNames[1].strip())
	    self.firstTeamName = firstTeamName
	    self.secondTeamName = secondTeamName
	    return self.firstTeamName + " v " + self.secondTeamName

	def checkCategory(self,teamName):
		if teamName == 'TBC':
			pass
		else:
			print "team name here: ",teamName
			ids = c.execute("SELECT Rank From iplPoints where Teams = '%s';" % teamName)
			return str(ids)



	def getFixturesWithShortNames(self):
		tree = lxml.html.parse(self.url)
		dates = tree.xpath(
		    "//li[@class='large-20 medium-20 columns']/div[1]/span/text()")
		countGame = 0

		for i in range(0, len(dates)):
		    if (i % 2 == 0):
		        date_string = dates[i].strip() + ' ' + \
		            dates[i + 1].split(u'\xa0')[0] + '+0530 2017'
		        dt = parser.parse(date_string)
		        c.execute("insert into fixtures (game,deadline, team1Category, team2Category) values (?,?,?,?)", [
		                  self.convertTeamNameIntoShortName(self.gameScheduleList[countGame].split('-')[1]), dt.astimezone(HERE), self.checkCategory(self.firstTeamName), self.checkCategory(self.secondTeamName)])
		        countGame = countGame + 1

fixtures = Fixtures("http://www.espncricinfo.com/indian-premier-league-2017/content/series/1078425.html?template=fixtures",[])
fixtures.getFullSchedule()
fixtures.getFixturesWithShortNames()

conn.commit()
conn.close()

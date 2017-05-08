import lxml.html
import prettytable
import sqlite3

conn = sqlite3.connect('iplPoints.db')
c = conn.cursor()


class PointTable:
	def __init__(self, url):
		self.url = url

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
	    return conversion[teamName]

	def get_pointtable(self):
		tree = lxml.html.parse(self.url)
		tabInfo = tree.xpath(
		    "//div[@class='large-20 medium-20 hide-for-small'][1]/table/tbody/tr")
		count = 1
		for trElem in tabInfo[1:]:
		    row = []
		    for td in trElem:
		        row.append(td.text.rstrip())

		    c.execute("insert into iplPoints (Rank, Teams, MAT, WON,LOST, TIED, NR, PTS, NETRR, FOR, AGAINST) values (?,?,?,?,?,?,?,?,?,?,?)", [
		              count,self.conversion(row[0].strip()), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])
		    count = count + 1

# print "IPL Point Table: \n", (table)

iplPointTable = PointTable("http://www.espncricinfo.com/indian-premier-league-2017/engine/series/1078425.html?view=pointstable")
iplPointTable.get_pointtable()
conn.commit()
conn.close()

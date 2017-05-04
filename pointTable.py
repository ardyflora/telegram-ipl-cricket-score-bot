import sqlite3
from datetime import datetime
import lxml.html
from dateutil import parser
from dateutil import tz
import prettytable

HERE = tz.tzlocal()


pointTableUrl = 'http://www.espncricinfo.com/indian-premier-league-2017/engine/series/1078425.html?view=pointstable'



tree = lxml.html.parse(pointTableUrl)
tabInfo = tree.xpath("//div[@class='large-20 medium-20 hide-for-small'][1]/table/tbody/tr")

#Adding prettytable
table = prettytable.PrettyTable(['Teams', 'MAT', 'WON', 'LOST', 'TIED','N/R', 'PTS', 'NET RR','FOR','AGAINST'])


for trElem in tabInfo[1:]:
	row = []
	for td in trElem:
		row.append(td.text.rstrip())

	table.add_row(row)



print "IPL Point Table: \n",table


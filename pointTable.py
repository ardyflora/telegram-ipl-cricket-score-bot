import lxml.html
import prettytable
import sqlite3

conn = sqlite3.connect('iplPoints.db')
c = conn.cursor()

pointTableUrl = 'http://www.espncricinfo.com/indian-premier-league-2017/engine/series/1078425.html?view=pointstable'


tree = lxml.html.parse(pointTableUrl)
tabInfo = tree.xpath(
    "//div[@class='large-20 medium-20 hide-for-small'][1]/table/tbody/tr")

for trElem in tabInfo[1:]:
    row = []
    for td in trElem:
        row.append(td.text.rstrip())

    c.execute("insert into iplPoints (Teams, MAT, WON,LOST, TIED, NR, PTS, NETRR, FOR, AGAINST) values (?,?,?,?,?,?,?,?,?,?)", [
              row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])


# print "IPL Point Table: \n", table

conn.commit()
conn.close()

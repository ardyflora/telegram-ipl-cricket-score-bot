import sqlite3


def create_iplPoints(c):
    c.execute('''CREATE TABLE iplPoints
              (Rank integer, Teams text, MAT integer, WON integer, Lost integer, TIED integer, NR integer , PTS integer, NETRR text, FOR text, AGAINST text)''')

# Create fixtures table
# game: Fixtures
# deadline: future timestamp when activity should occur
#
# example:
#__________________________________________
# id | deadline  | game        |
# 1 | date      | RCB vs KKR  |
# 2 | date      | MI vs KXIP  |


def create_fixtures(c):
    c.execute('''CREATE TABLE fixtures
              (id integer primary key, game text, deadline ts, team1Category integer, team2Category integer)''')


def init_database():
    conn = sqlite3.connect('iplPoints.db')
    c = conn.cursor()
    create_iplPoints(c)
    create_fixtures(c)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_database()

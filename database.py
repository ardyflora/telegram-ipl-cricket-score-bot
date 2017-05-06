import sqlite3


def create_iplPoints(c):
    c.execute('''CREATE TABLE iplPoints
              (Teams text, MAT integer, WON integer, Lost integer, TIED integer, NR integer , PTS integer, NETRR text, FOR text, AGAINST text)''')


def init_database():
    conn = sqlite3.connect('iplPoints.db')
    c = conn.cursor()
    create_iplPoints(c)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_database()

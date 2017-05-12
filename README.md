# Telegram-IPL-cricket-score-bot

> A Telegram bot that gives you the latest IPL cricket scores from Cricinfo.

Some of the cool features:
* **/fixtures** - display next 5 day fixtures
* **/iplpoints** - display latest point table

Please refer to screenshots below to see `telegram IPL cricket score bot` in action:

![IPL Fixture in telegram bot](https://snag.gy/uoBcxK.jpg)
![IPL Points in telegram bot](https://snag.gy/5IPNvx.jpg)

## Benefits
* You don't have to browse through the *cricinfo website* to find the latest IPL points table, with just one command you will get the immediate update.
* *Cricinfo IPL fixtures* webpage will show you the full schedule, which makes it tedious to scroll down and look for upcoming fixtures but with the `telegram IPL cricket score bot` you will be able to see next 5 day fixtures with just one command 


## Features to be added
* `/currentScore` - Scrapes the current score for today's game(live)
* `/manOfTheMatch` - Returns MOM for today's game
* `/highestRun` - Player who scored highest runs in today's game
* `/highestWicketsTaken` - Player who took highest number of wicket's in today's game
* `/sixes` - Total number of sixes hit in the game (For both the team's combined)
* `/fours` - Total number of boundaries hit in the game
* `/maidens` - Any maidens over delivered
* `/hat-trick` - Any hat-tricks taken in the game

## Installation
* You will need to install python telegram bot
  * Please follow the link:  
    https://github.com/python-telegram-bot/python-telegram-bot
* PrettyTable - Which is used to display the result as shown in the **telegram Ipl cricket score bot screenshot** above
   * To install PrettyTable, Please follow: https://pypi.python.org/pypi/PrettyTable
* lmxl - which is used to scrape the cricinfo website
   * To install lxml, Please follow: http://lxml.de/installation.html

## How to Execute?
* Execute in following order:
  
  `python database.py` - This will create the *iplPoints.db* file. 

  `python pointTable.py` - This will insert iplPoint Table into iplPoints.db

  `python fixtures.py` - This will insert fixtures Tables into iplPoints.db

  `python interface.py` - Once this is running, you can go to telegram and open **pointTableCricinfo bot** where you can type `/start` to start the telegram bot, it should return _I'm a bot, please talk to me!_. Once you can see  that, you can run any of the two commands `/fixtures` or `/iplpoints`

## Release History
* 0.0.1
    * Work in progress

## Meta

Ardy Flora – flora_ripudaman@hotmail.com

Distributed under the MIT license. See ``LICENSE.txt`` for more information.

[https://github.com/ardyflora/telegram-ipl-cricket-score-bot](https://github.com/ardyflora/)

## Contributing

1. Fork it (<https://github.com/ardyflora/telegram-ipl-cricket-score-bot>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

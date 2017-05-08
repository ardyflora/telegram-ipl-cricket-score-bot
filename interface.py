from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import sqlite3
import prettytable

updater = Updater(token='345858240:AAGwmVex4IOZntM48kWWVQH-plFbR3RiQxU')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

dispatcher = updater.dispatcher


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="I'm a bot, please talk to me!")


def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)


def iplpoints(bot, update):
    table = []
    conn = sqlite3.connect('iplPoints.db')
    c = conn.cursor()
    # Add in prettytable
    table = prettytable.PrettyTable(
        ['Rank','Teams', 'MAT', 'WON', 'LOST', 'TIED', 'N/R', 'PTS', 'NET RR', 'FOR', 'AGAINST'])
    ipPoints = c.execute('SELECT * from iplPoints')
    for el in ipPoints:
        table.add_row(el)
    bot.sendMessage(chat_id=update.message.chat_id, text=str(table))


def fixtures(bot, update):
	table = []
	conn = sqlite3.connect('iplPoints.db')
	c = conn.cursor()
	# Add in prettytable
	table = prettytable.PrettyTable(
	['Game','Deadline'])
	fixtures = c.execute('SELECT game,deadline FROM fixtures WHERE deadline BETWEEN date(\'now\') and date(\'now\', \'+5 day\')')
	for el in fixtures:
		table.add_row(el)
	bot.sendMessage(chat_id=update.message.chat_id, text=str(table))

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

iplPoints_handler = CommandHandler('iplpoints', iplpoints)
dispatcher.add_handler(iplPoints_handler)

fixtures_handler = CommandHandler('fixtures', fixtures)
dispatcher.add_handler(fixtures_handler)

updater.start_polling()

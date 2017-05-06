from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
import logging
import sqlite3
import prettytable

updater = Updater(token='345858240:AAGwmVex4IOZntM48kWWVQH-plFbR3RiQxU')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

dispatcher = updater.dispatcher

# Add in prettytable
table = prettytable.PrettyTable(['Teams', 'MAT', 'WON', 'LOST', 'TIED', 'N/R', 'PTS', 'NET RR', 'FOR', 'AGAINST'])

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
	text_caps = ' '.join(args).upper()
	bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

def readIplPointsFromDatabase():
	conn = sqlite3.connect('iplPoints.db')
	c = conn.cursor()
	ipPoints = c.execute('SELECT * from iplPoints')
	for el in ipPoints:
		table.add_row(el)

def iplpoints(bot, update):
	readIplPointsFromDatabase()
	print "table now: ",table
	newList = str(table)
	print "New list: ",newList
	bot.sendMessage(chat_id=update.message.chat_id, text=newList)



start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

iplPoints_handler = CommandHandler('iplpoints', iplpoints)
dispatcher.add_handler(iplPoints_handler)

updater.start_polling()

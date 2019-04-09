'''
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater,InlineQueryHandler, CommandHandler,MessageHandler,Filters,CallbackQueryHandler
import requests
import re


def get_title(t):
    print("here1")
    print(t)
    contents = requests.get('http://www.omdbapi.com/?t=house of cards&apikey=9b24e033').json()
    title = contents['Title']
    print(title)
    return title

def bop(bot, context):
	print("faidjf")
	title =get_title()
	chat_id =context.message.chat_id
	#context.message.reply_text(title)
	#bot.send_chat_action(chat_id=context.message.chat_id, action=ChatAction.TYPING)
	bot.send_message(chat_id =chat_id, text =title)


def start(update, context):
	keyboard =[[InlineKeyboardButton("Title", callback_data='1'),
				InlineKeyboardButton("IMDB Rating", callback_data='2')]]
	reply_markup = InlineKeyboardMarkup(keyboard)
	context.message.reply_text('Retrieve any information regarding Movies!', reply_markup=reply_markup)

def button(update,context):
	query =context.callback_query.data	
	print(query)
	if query=='1':
		print("here")
		get_title(t)
		print("done")
	else:
		print("done forever")

def add(update, context, msg):
    chat_id =context.message.chat_id
    send1 = update.send_message(chat_id,'whats your name?')
    if send1:
        text1 = msg['text']
        print(text1)

def convert_uppercase(update, context):
	print("here2")
	context.message.reply_text(msg)


def main():
	updater =Updater('707919520:AAE51Xcv4q3P0m7e83urLeTQrwwTG_iR8zo')
	dp =updater.dispatcher
	#dp.add_handler(CommandHandler('start',start))
	dp.add_handler(CommandHandler('add',add))
	#dp.add_handler(CallbackQueryHandler(button))
	dp.add_handler(MessageHandler(Filters.text, get_title))
	dp.add_handler(MessageHandler(Filters.text, bop))
	#dp.add_handler(CommandHandler('title',bop))
	updater.start_polling()
	updater.idle()

if __name__=='__main__':
	main()
'''

import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import requests

def convert_uppercase(bot, update):
    text =update.message.text
    url ='http://www.omdbapi.com/?t='+text+'&apikey=9b24e033'
    contents = requests.get(url).json()
    title = contents
    print(title)
    chat_id =update.message.chat_id
    bot.send_message(chat_id =chat_id, text =title)    



def start(update, context):
    keyboard = [[InlineKeyboardButton("Movie Name", callback_data='1'),
                 InlineKeyboardButton("IMDB Rating", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    context.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update, context):
    choice = context.callback_query.data
    query =context.callback_query
    if choice=='1':
    	query.edit_message_text(text="Enter Movie Title")
    else:
    	query.edit_message_text(text="Enter IMDB rating")


def help(update, context):
    context.message.reply_text("Use /start to test this bot.")


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("TOKEN")

    updater.dispatcher.add_handler(CommandHandler('search', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, convert_uppercase))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

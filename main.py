from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import requests

def get_info(update, context):
    chat_id =context.message.chat_id
    text =context.message.text
    url ='http://www.omdbapi.com/?t='+text+'&apikey=9b24e033'
    contents = requests.get(url).json()
    if(contents['Response']=="False"):
    	update.send_message(chat_id=chat_id, text="Movie not found. Try again")
    	return
    title = contents['Title']
    actors =contents['Actors']
    year =contents['Year']
    genre =contents['Genre']
    awards =contents['Awards']
    poster =contents['Poster']
    ratings_IMDB =contents['imdbRating']
    output ="Name: " +title +"\n" + "Released in the year " +year +"\n" + "Actors: " + actors +"\n" + "Awards: " + awards +"\n" + "Genre: "+genre +"\n" + "IMDB: " + ratings_IMDB +"\n" + poster
    update.send_message(chat_id =chat_id, text =output)
    return

def start(update, context):
    context.message.reply_text('Enter name to get details')
    return 

def help(update, context):
    context.message.reply_text("Use /search to start this bot.")


def unknown(update, context):
	chat_id =context.message.chat_id
	update.send_message(chat_id =chat_id, text ="Invalid command: Please start with /search")


def main():
    updater = Updater("TOKEN")

    updater.dispatcher.add_handler(CommandHandler('search', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, get_info))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    # Start the Bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
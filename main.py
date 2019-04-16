from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import requests

def get_info(update, context):
    chat_id =context.message.chat_id
    text =context.message.text
    url ='http://www.omdbapi.com/?t='+text+'&apikey=9b24e033'
    contents = requests.get(url).json()
    title = contents['Title']
    actors =contents['Actors']
    year =contents['Year']
    genre =contents['Genre']
    awards =contents['Awards']
    poster =contents['Poster']
    ratings_Rotten =contents['Ratings'][1]['Value']
    ratings_IMDB =contents['imdbRating']
    output ="Name: " +title +"\n" + "Released in the year " +year +"\n" + "Actors: " + actors +"\n" + "Awards: " + awards +"\n" + "Genre: "+genre +"\n" + "Rotten Tomatoes: " +ratings_Rotten + "\n" + "IMDB: " + ratings_IMDB +"\n" + poster
    
    update.send_message(chat_id =chat_id, text =output)


def start(update, context):
    keyboard = [[InlineKeyboardButton("Movie/Series Name", callback_data='1'),
                 InlineKeyboardButton("IMDB Rating", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update, context):
    choice = context.callback_query.data
    query =context.callback_query
    print(query)
    if choice=='1':
    	query.edit_message_text(text="Enter Name")
    else:
    	query.edit_message_text(text="Enter IMDB Rating")

def help(update, context):
    context.message.reply_text("Use /search to start this bot.")


def unknown(update, context):
	chat_id =context.message.chat_id
	update.send_message(chat_id =chat_id, text ="Invalid command: Please start with /search")


def main():
    updater = Updater("707919520:AAE51Xcv4q3P0m7e83urLeTQrwwTG_iR8zo")

    updater.dispatcher.add_handler(CommandHandler('search', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, get_info))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
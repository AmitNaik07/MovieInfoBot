from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import requests

def get_info(bot, update):
    text =update.message.text
    url ='http://www.omdbapi.com/?t='+text+'&apikey=9b24e033'
    contents = requests.get(url).json()
    title = contents['Title']
    year =contents['Year']
    genre =contents['Genre']
    awards =contents['Awards']
    poster =contents['Poster']
    ratings_Rotten =contents['Ratings'][1]['Value']
    ratings_IMDB =contents['imdbRating']
    output =title +"\n" + "Released in the year " +year +"\n" + "Awards: " + awards +"\n" + "Genre: "+genre +"\n" + "Rotten Tomatoes: " +ratings_Rotten + "\n" + "IMDB: " + ratings_IMDB +"\n" + poster
    chat_id =update.message.chat_id
    bot.send_message(chat_id =chat_id, text =output)


def start(update, context):
    keyboard = [[InlineKeyboardButton("Movie Name", callback_data='1'),
    			 InlineKeyboardButton("Series Name", callback_data='2'),
                 InlineKeyboardButton("IMDB Rating", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    context.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update, context):
    choice = context.callback_query.data
    query =context.callback_query
    if choice=='1':
    	query.edit_message_text(text="Enter Movie Name")
    elif choice=='2':
    	query.edit_message_text(text="Enter Series Name")
    else:
    	query.edit_message_text(text="Enter IMDB Rating")


def help(update, context):
    context.message.reply_text("Use /start to test this bot.")


def main():
    updater = Updater("707919520:AAE51Xcv4q3P0m7e83urLeTQrwwTG_iR8zo")

    updater.dispatcher.add_handler(CommandHandler('search', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, get_info))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
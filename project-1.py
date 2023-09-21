from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    content = requests.get('http://javascript:void(0)').json()
    url = content['url']
    return url

def bop(bop, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id = chat_id, photo = url)

def main():
    updater = Updater('Your Token')
    dp = Updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_pulling()
    updater.idle()

if __name__ == '__main__':
    main()
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

updater = Updater(token='764096237:AAFJCh0TuxxjJ47peMMjpOTCVp4S-aGJcG0',request_kwargs={'proxy_url':'socks5://202.43.177.14:4145'})
print("Create updater")
start_handler = CommandHandler('start', start)
print("Create command handler")
updater.dispatcher.add_handler(start_handler)
print("Start polling")
updater.start_polling()
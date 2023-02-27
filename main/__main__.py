from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from . import send_greeting, button_click

def main():
    tkn = 'YOUR TOKEN HERE'
    updater = Updater(token=tkn, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', send_greeting)
    button_handler = CallbackQueryHandler(button_click)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(button_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()

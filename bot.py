from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from handlers import help, start, inline_query
import settings
import logging


class Bot():
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def error(self, update, context):
        self.logger.warning('Update "%s" caused error "%s"',
                            update, context.error)

    def run(self):
        updater = Updater(settings.TELEGRAM_TOKEN, use_context=True)

        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start.handle))
        dp.add_handler(CommandHandler("help", help.handle))
        dp.add_handler(InlineQueryHandler(inline_query.handle))
        dp.add_error_handler(self.error)

        updater.start_polling()
        updater.idle()

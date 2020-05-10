from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from bot.handlers import help, start, error, inline_query
from .settings import Settings

settings = Settings()


class Bot():
    def run(self):
        updater = Updater(settings.telegram_token(), use_context=True)

        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start.handle))
        dp.add_handler(CommandHandler("help", help.handle))
        dp.add_handler(InlineQueryHandler(inline_query.handle))
        dp.add_error_handler(error.handle)

        updater.start_polling()
        updater.idle()

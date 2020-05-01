from telegram import InlineQueryResultPhoto, ParseMode
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown
from emoji import emojize
from os import environ

from models import LegoSet

class Bot():
    def __init__(self, logger):
        self.logger = logger


    def start(self, update, context):
        cake = emojize(":imp:", use_aliases=True)
        update.message.reply_text('Welcome to the Brickminer bot. I\'m sorry but you will never be able to get info for the set 60115 ' + cake)


    def help(self, update, context):
        cake = emojize(":imp:", use_aliases=True)
        update.message.reply_text('I\'m sorry but you will never be able to get info for the set 60115 ' + cake)


    def inline_query(self, update, context):
        self.logger.info(update)
        query = update.inline_query.query

        results = []
        if len(query) > 3:
            lego_sets = LegoSet.search(query)
            if len(lego_sets) > 0:
                for lego_set in lego_sets:
                    set_info = lego_set.set_info()

                    results.append(
                        InlineQueryResultPhoto(
                            id=lego_set.id,
                            title=lego_set.number,
                            description=set_info,
                            caption=set_info,
                            photo_url=lego_set.image,
                            thumb_url=lego_set.image
                        )
                    )    

                update.inline_query.answer(results)


    def error(self, update, context):
        self.logger.warning('Update "%s" caused error "%s"', update, context.error)


    def run(self):
        updater = Updater(environ.get("TELEGRAM_TOKEN"), use_context=True)

        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(CommandHandler("help", self.help))
        dp.add_handler(InlineQueryHandler(self.inline_query))
        dp.add_error_handler(self.error)
        
        updater.start_polling()
        updater.idle()
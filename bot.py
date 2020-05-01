import logging
from uuid import uuid4
from telegram import InlineQueryResultPhoto, ParseMode
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown
from emoji import emojize
from os import environ
from babel.numbers import format_decimal

from models import LegoSet

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    cake = emojize(":imp:", use_aliases=True)
    update.message.reply_text('Welcome to the Brickminer bot. I\'m sorry but you will never be able to get info for the set 60115 ' + cake)


def help(update, context):
    cake = emojize(":imp:", use_aliases=True)
    update.message.reply_text('I\'m sorry but you will never be able to get info for the set 60115 ' + cake)


def inlinequery(update, context):
    logger.info(update)
    query = update.inline_query.query

    results = []
    if len(query) > 3:
        lego_sets = LegoSet.search(query)
        if len(lego_sets) > 0:
            for lego_set in lego_sets:
                set_info = get_set_info(lego_set)    

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

            logger.info(len(results))
            update.inline_query.answer(results)

def get_set_info(lego_set):
    template = "Set Number: {}\nName: {}\nParts: {}\nMinifigs: {}\nYear: {}\nUS Price: {}\nEU Price: {}\nUK Price: {}"

    return template.format(
        lego_set.number, 
        lego_set.name, 
        lego_set.pieces, 
        lego_set.minifigs, 
        lego_set.year, 
        format_decimal(lego_set.us_price, locale='en_US'), 
        format_decimal(lego_set.eu_price, locale='en_US'), 
        format_decimal(lego_set.uk_price, locale='en_US')
    )


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(environ.get("TELEGRAM_TOKEN"), use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(InlineQueryHandler(inlinequery))
    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
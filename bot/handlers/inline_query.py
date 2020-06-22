from telegram import InlineQueryResultPhoto
from bot.database.models import LegoSet
from bot.generators import meme
from bot.factory.iqrp_factory import IQRP_Factory
from bot.factory.not_found_factory import NotFoundFactory
from bot.generators.meme import Meme

factory = IQRP_Factory(Meme())
not_found_factory = NotFoundFactory()

def handle(update, context):
    query = update.inline_query.query

    results = []
    if len(query) > 3:
        sets = LegoSet.search(query)
        if len(sets) > 0:
            for lego_set in sets:
                results.append(factory.create(lego_set))

            update.inline_query.answer(results)
        else:
            response = [not_found_factory.create()]
            update.inline_query.answer(response)

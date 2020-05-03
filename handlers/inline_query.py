from telegram import InlineQueryResultPhoto
from models import LegoSet
from generators import meme


def handle(update, context):
    query = update.inline_query.query

    results = []
    if len(query) > 3:
        lego_sets = LegoSet.search(query)
        if len(lego_sets) > 0:
            for lego_set in lego_sets:
                set_info = lego_set.set_info()

                if lego_set.is_blocked():
                    lego_set.image = meme.image_link()
                    set_info = meme.bad_text()

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

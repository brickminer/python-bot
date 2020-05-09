from bot.database.models import LegoSet
from telegram import InlineQueryResultPhoto


class IQRP_Factory():
    def __init__(self, meme):
        self.meme = meme

    def create(self, set: LegoSet) -> InlineQueryResultPhoto:
        info = set.set_info()

        if set.is_blocked():
            set.image = self.meme.image_link()
            info = self.meme.bad_text(set.name)

        return InlineQueryResultPhoto(
            id=set.id,
            title=set.number,
            description=info,
            caption=info,
            photo_url=set.image,
            thumb_url=set.image
        )

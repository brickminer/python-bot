from telegram import InlineQueryResultPhoto


class NotFoundFactory():
    def create(self, query: str) -> InlineQueryResultPhoto:
        message = f'Set {query} not found'

        return InlineQueryResultPhoto(
            id='not_found',
            title=message,
            description=message,
            caption=message,
            photo_url='https://i.pinimg.com/originals/ca/9e/eb/ca9eebb9c935248dba2deeff760dec83.jpg',
            thumb_url='https://i.pinimg.com/originals/ca/9e/eb/ca9eebb9c935248dba2deeff760dec83.jpg'
        )

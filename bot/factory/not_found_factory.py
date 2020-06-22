from telegram import InlineQueryResultPhoto


class NotFoundFactory():
    def create(self) -> InlineQueryResultPhoto:
        return InlineQueryResultPhoto(
            id='not_found',
            title='Set not found',
            description='Set not found',
            caption='Set not found',
            photo_url='https://i.pinimg.com/originals/ca/9e/eb/ca9eebb9c935248dba2deeff760dec83.jpg',
            thumb_url='https://i.pinimg.com/originals/ca/9e/eb/ca9eebb9c935248dba2deeff760dec83.jpg'
        )

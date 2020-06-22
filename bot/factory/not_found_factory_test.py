from bot.factory.not_found_factory import NotFoundFactory
from telegram import InlineQueryResultPhoto


def test_create_not_found_response():
    factory = NotFoundFactory()
    result = factory.create('1111-1')

    assert type(result) is InlineQueryResultPhoto
    assert result.id == 'not_found'
    assert result.title == 'Set 1111-1 not found'
    assert result.description == 'Set 1111-1 not found'
    assert result.caption == 'Set 1111-1 not found'
    assert result.photo_url == 'https://i.pinimg.com/originals/ca/9e/eb/ca9eebb9c935248dba2deeff760dec83.jpg'
    assert result.thumb_url == 'https://i.pinimg.com/originals/ca/9e/eb/ca9eebb9c935248dba2deeff760dec83.jpg'
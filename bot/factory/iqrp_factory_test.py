import pytest
from bot.factory.iqrp_factory import IQRP_Factory
from telegram import InlineQueryResultPhoto
from mock import patch
from bot.database.models import LegoSet


@pytest.fixture()
def info() -> str:
    return """Set Number: 123-1
            Name: name
            Parts: 1000
            Minifigs: 5
            Year: 2000
            US Price: $5.00
            EU Price: €5.00
            UK Price: £5.00"""


@pytest.fixture()
@patch("bot.database.models.LegoSet")
def set_mock(set_mock):
    set_mock.id = 123
    set_mock.number = "123-1"
    set_mock.image = "photo.jpg"

    return set_mock


@patch("bot.generators.meme.Meme")
def test_create_without_blocked_set(meme_mock, set_mock, info):
    set_mock.is_blocked.return_value = False
    set_mock.set_info.return_value = info

    factory = IQRP_Factory(meme_mock)
    result = factory.create(set_mock)

    assert type(result) is InlineQueryResultPhoto
    assert result.id == "123"
    assert result.title == "123-1"
    assert result.description == info
    assert result.caption == info
    assert result.photo_url == "photo.jpg"
    assert result.thumb_url == "photo.jpg"


@patch("bot.generators.meme.Meme")
def test_create_with_blocked_set(meme_mock, set_mock):
    meme_mock.bad_text.return_value = "Bad Text"
    meme_mock.image_link.return_value = "bad.jpg"
    set_mock.is_blocked.return_value = True

    factory = IQRP_Factory(meme_mock)
    result = factory.create(set_mock)

    assert type(result) is InlineQueryResultPhoto
    assert result.id == "123"
    assert result.title == "123-1"
    assert result.description == "Bad Text"
    assert result.caption == "Bad Text"
    assert result.photo_url == "bad.jpg"
    assert result.thumb_url == "bad.jpg"

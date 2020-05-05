import pytest
from bot.generators import meme


def test_image_link():
    image = meme.image_link()
    assert image in meme.images


def test_bad_text():
    text = meme.bad_text('some set')
    assert 'some set' in text

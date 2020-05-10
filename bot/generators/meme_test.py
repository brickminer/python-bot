import pytest
from bot.generators.meme import Meme


def test_image_link():
    meme = Meme()
    image = meme.image_link()
    assert image in meme.images


def test_bad_text():
    meme = Meme()
    text = meme.bad_text('some set')
    assert 'some set' in text

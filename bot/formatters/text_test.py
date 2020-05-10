import pytest
from bot.formatters import text


def test_format():
    assert text.format(None) == 'N/A'
    assert text.format('') == 'N/A'
    assert text.format('some text') == 'some text'

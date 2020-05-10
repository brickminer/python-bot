import pytest
from bot.formatters import currency


def test_format():
    assert currency.format(None) == 'N/A'
    assert currency.format('0.00', 'USD') == 'N/A'
    assert currency.format(5, 'USD') == '$5.00'
    assert currency.format(5, 'EUR') == '€5.00'
    assert currency.format(5, 'GBP') == '£5.00'

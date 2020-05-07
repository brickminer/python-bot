import pytest
from bot.handlers import help
from mock import patch


@patch("bot.settings.Settings.blocked_sets")
@patch("telegram.Message")
@patch("telegram.Update")
def test_handle_without_blocked_sets(update_mock, message_mock, blocked_sets_mock):
    blocked_sets_mock.return_value = []
    update_mock.message = message_mock

    help.handle(update_mock, {})

    message_mock.reply_text.assert_called_once_with(
        "To search for a set, just type @brickminerbot + set number or set name. You should be presented to a list of results, just select the one you wan't to show.")


@patch("bot.settings.Settings.blocked_sets")
@patch("telegram.Message")
@patch("telegram.Update")
def test_handle_with_blocked_sets(update_mock, message_mock, blocked_sets_mock):
    blocked_sets_mock.return_value = ['111', '222']
    update_mock.message = message_mock

    help.handle(update_mock, {})

    message_mock.reply_text.assert_called_once_with(
        "To search for a set, just type @brickminerbot + set number or set name. You should be presented to a list of results, just select the one you wan't to show.\nI'm sorry but you will never be able to get info for the 111, 222, they are 👿")

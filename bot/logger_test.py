from .logger import Logger
from mock import patch
import logging


@patch("logging.basicConfig")
def test_default_logger(config_mock):
    logger = Logger()
    logger.getLogger().info("message")

    config_mock.assert_called_once_with(
        filename=Logger.FILENAME, level=logging.DEBUG, format=Logger.FORMAT)


@patch("logging.basicConfig")
def test_custom_logger(config_mock):
    logger = Logger('file.log', logging.INFO, '%(message)')
    logger.getLogger().info("message")

    config_mock.assert_called_once_with(
        filename="file.log", level=logging.INFO, format="%(message)")

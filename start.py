import logging
from bot.bot import Bot
from bot.logger import logger


def main():
    logger.debug('Initializing Telegram Bot')
    bot = Bot()
    bot.run()


if __name__ == '__main__':
    main()

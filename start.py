import logging
from bot.bot import Bot
from bot.logger import Logger


def main():
    logger = Logger()
    bot = Bot()

    logger.getLogger().debug('Initializing Telegram Bot')
    bot.run()


if __name__ == '__main__':
    main()

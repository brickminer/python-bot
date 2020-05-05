import logging
from bot.bot import Bot
from bot import logger


def main():
    bot = Bot(logger)
    bot.run()


if __name__ == '__main__':
    main()

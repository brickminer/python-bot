from bot.logger import Logger


def handle(update, context):
    logger = Logger()
    logger.getLoggert().warning('Update "%s" caused error "%s"', update, context.error)

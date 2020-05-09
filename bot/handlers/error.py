from bot.logger import Logger


def handle(update, context):
    logger = Logger()
    logger.getLogger().warning('Update "%s" caused error "%s"', update, context.error)

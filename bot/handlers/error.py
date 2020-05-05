from ..logger import logger


def handle(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
